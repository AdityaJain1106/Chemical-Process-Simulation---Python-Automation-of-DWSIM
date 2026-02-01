import clr

clr.AddReference(r"C:\Program Files\DWSIM\DWSIM.UnitOperations.dll")

import System

for asm in System.AppDomain.CurrentDomain.GetAssemblies():
    if "UnitOperations" in asm.FullName:
        for t in asm.GetTypes():
            if "Stream" in t.FullName or "Material" in t.FullName:
                print(t.FullName)
                