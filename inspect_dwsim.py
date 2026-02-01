import clr

clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.Automation.dll")
clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.UnitOperations.dll")
clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.Thermodynamics.dll")
clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.SharedClasses.dll")

import System

for asm in System.AppDomain.CurrentDomain.GetAssemblies():
    if "DWSIM" in asm.FullName:
        print("=== Assembly:", asm.FullName, "===")
        for t in asm.GetTypes():
            print(t.FullName)