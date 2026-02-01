
````markdown
# DWSIM Python Automation Task


## 📘 About the Project

This repository contains the **DWSIM Python Automation Task**, where Python is used to automate a DWSIM flowsheet, modify input values, run simulations programmatically, and extract results into a CSV file.

This project helps you:
- Automate repetitive simulation tasks  
- Modify DWSIM flowsheet variables using Python  
- Run the simulation engine via scripting  
- Export results (streams, equipment parameters, etc.) into CSV  
- Build a reusable automation template for future engineering simulations

If you're working with process simulation + automation, this project saves time and ensures reproducible results.

---

## 🖼 Project Snapshot

> *(Add screenshots here if needed — flowsheet, Python output, CSV output, etc.)*

---

## 🛠 Built With

This project uses the following tools/libraries:

- **Python 3.x**
- **DWSIM** (Open-source Chemical Process Simulator)
- **DWSIM Python Plugin / Automation API**
- **pandas** (for CSV creation)
- **.NET assemblies used by DWSIM automation**

---

## 🚀 Getting Started

Follow this guide to set up the project locally.

---

### ✔ Prerequisites

Make sure you have the following installed:

- **DWSIM (latest version)**  
  Download: https://dwsim.org
- **Python 3.x**
- Required Python libraries:
  ```bash
  pip install pandas pythonnet
````

* A **DWSIM Flowsheet Template (.dwxmz)**
  This project uses your template named:
  `flowsheet_template.dwxmz`

---

## 📥 Installation & Setup

### 1️⃣ **Fork This Repository**

Click the “Fork” button on GitHub to create your own copy.

### 2️⃣ **Clone the Repository**

```bash
git clone https://github.com/your_username/DWSIM-Python-Automation.git
cd DWSIM-Python-Automation
```

### 3️⃣ **Add Your DWSIM Files**

Inside the project folder, add:

* `flowsheet_template.dwxmz`
* Any required `.dll` files (if needed)

### 4️⃣ **Install Required Python Packages**

```bash
pip install pandas pythonnet
```

### 5️⃣ **Run the Automation Script**

```bash
python dwsim_automation.py
```

This script will:

* Load your DWSIM flowsheet
* Modify input parameters
* Run simulation
* Extract stream & equipment data
* Generate:
  → `results_output.csv`

---

## 📌 Usage

This is how the automation workflow runs:

```text
1. Load DWSIM flowsheet template
2. Modify variables (flowrate, pressure, temperature, etc.)
3. Execute DWSIM solver using Python
4. Read output (streams, unit operations)
5. Save results to CSV
```

Example automation snippet:

```python
flowsheet = sim.LoadFlowsheet("flowsheet_template.dwxmz")
stream = flowsheet.GetObject("Material Stream 1")

stream.Temperature = 350
stream.Pressure = 5

flowsheet.Run()
flowsheet.SaveResults("results_output.csv")
```

---

## 🗺 Roadmap

* [ ] Add GUI to load flowsheet and run simulation
* [ ] Generate plots of temperature/pressure changes
* [ ] Add multiple automated case-runs
* [ ] Cloud execution support
* [ ] Add unit tests
* [ ] Add documentation wiki

Check the Issues tab for more planned improvements.

---

## 🤝 Contributing

Contributions are always welcome!

### How to Contribute

1. Fork the project
2. Create your branch:

   ```bash
   git checkout -b feature/NewFeature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Added NewFeature"
   ```
4. Push your branch:

   ```bash
   git push origin feature/NewFeature
   ```



## 📬 Contact

**Aditya Jain**
📎 LinkedIn: *[https://www.linkedin.com/in/adddijain/](https://www.linkedin.com/in/adddijain/)*
📧 Email: *adijain1106@gmail.com*

Project Link:
[https://github.com/AdityaJain1106/Chemical-Process-Simulation---Python-Automation-of-DWSIM](https://github.com/AdityaJain1106/Chemical-Process-Simulation---Python-Automation-of-DWSIM)

---

## ⭐ Acknowledgments

Some helpful references:

* DWSIM Official Documentation
* PythonNET
* Img Shields
* GitHub README Templates
* Pandas Library

---

*(back to top)*
