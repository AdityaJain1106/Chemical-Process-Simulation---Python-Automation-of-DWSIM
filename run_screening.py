import clr
import os
import traceback
import csv

# -----------------------------
#  LOAD AUTOMATION DLL
# -----------------------------

clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.Automation.dll")
clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.SharedClasses.dll")
clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.Thermodynamics.dll")
clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.UnitOperations.dll")

from DWSIM.Automation import Automation2

# -----------------------------
#  HELPER FUNCTIONS
# -----------------------------

def safe_run(fn, params):
    try:
        return fn(**params)
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "trace": traceback.format_exc()
        }

def write_csv(fname, rows, header):
    new = not os.path.exists(fname)
    with open(fname, "a", newline="") as f:
        w = csv.DictWriter(f, header)
        if new:
            w.writeheader()
        for r in rows:
            w.writerow(r)

# -----------------------------
#  LOAD TEMPLATE
# -----------------------------

TEMPLATE = "template.dwxmz"
auto = Automation2()

# -----------------------------
#  PART A — PFR SIMULATION
# -----------------------------

def run_pfr_case(volume, temp):
    sim = auto.LoadFlowsheet(TEMPLATE)

    # Get objects from flowsheet
    feed = sim.GetMaterialStream("Feed")
    pfr = sim.GetObject("PFR")
    pfr_out = sim.GetMaterialStream("PFR_Out")

    # Set feed conditions
    feed.SetTemperature(temp)
    feed.SetMassFlow(1.0)
    feed.SetPressure(101325)

    # Set PFR conditions
    pfr.SetVolume(volume)
    pfr.SetIsothermal(True)
    pfr.SetTemperature(temp)

    # Run
    sim.RunSilent()

    # Output values
    A_in = feed.GetMassFlow("A")
    A_out = pfr_out.GetMassFlow("A")

    conversion = 1 - (A_out / A_in)

    return {
        "success": True,
        "error": "",
        "pfr_volume": volume,
        "pfr_temp": temp,
        "conversion": conversion,
        "A_out": A_out,
        "B_out": pfr_out.GetMassFlow("B"),
        "outlet_temp": pfr_out.GetTemperature(),
    }

# -----------------------------
#  PART B — DISTILLATION COLUMN
# -----------------------------

def run_column_case(stages, reflux):
    sim = auto.LoadFlowsheet(TEMPLATE)

    col = sim.GetObject("Column")
    feed = sim.GetMaterialStream("PFR_Out")
    dist = sim.GetMaterialStream("Column_Distillate")
    bot = sim.GetMaterialStream("Column_Bottoms")

    # Set column inputs
    col.NumberOfStages = stages
    col.RefluxRatio = reflux

    sim.RunSilent()

    return {
        "success": True,
        "error": "",
        "stages": stages,
        "reflux": reflux,
        "distillate_A": dist.GetMassFraction("A"),
        "bottoms_B": bot.GetMassFraction("B"),
        "condenser_duty": col.CondenserDuty,
        "reboiler_duty": col.ReboilerDuty
    }

# -----------------------------
#  MAIN PARAMETRIC SWEEP
# -----------------------------

def main():
    results_csv = "results.csv"

    header = [
    "case", "success", "error", "trace",

    "pfr_volume", "pfr_temp",
    "conversion", "A_out", "B_out", "outlet_temp",

    "stages", "reflux",
    "distillate_A", "bottoms_B",
    "condenser_duty", "reboiler_duty"
]

    rows = []

    # ---- PFR sweep ----
    volumes = [1, 2, 3]
    temps = [350, 400, 450]

    for V in volumes:
        for T in temps:
            r = safe_run(run_pfr_case, {"volume": V, "temp": T})
            r["case"] = "PFR"
            rows.append(r)

    # ---- Column sweep ----
    stages_list = [10, 15]
    reflux_list = [1.2, 1.5]

    for S in stages_list:
        for R in reflux_list:
            r = safe_run(run_column_case, {"stages": S, "reflux": R})
            r["case"] = "COLUMN"
            rows.append(r)

    write_csv(results_csv, rows, header)
    print("✔ Simulation complete — results saved to results.csv")

if __name__ == "__main__":
    main()


# OPTIONAL PLOTTING
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("plots", exist_ok=True)

df = pd.read_csv("results.csv")
pfr = df[df["case"] == "PFR"]

plt.plot(pfr["pfr_volume"], pfr["conversion"], marker="o")
plt.xlabel("Reactor Volume (m³)")
plt.ylabel("Conversion")
plt.title("PFR Conversion vs Volume")
plt.savefig("plots/pfr_conversion_vs_volume.png")
plt.close()