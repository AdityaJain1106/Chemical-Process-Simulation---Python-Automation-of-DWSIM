# Screening Task 2 – Python Automation of DWSIM

## 1. Overview
This project controls DWSIM using Python Automation API to perform:
- Plug Flow Reactor (PFR) simulation
- Distillation Column simulation
- Parametric sweeps
- Headless execution (no GUI)
- Automated results logging

## 2. Requirements
- Windows OS
- DWSIM installed
- Python 3.9+
- DWSIM.Automation.dll located at:
  C:\Program Files\DWSIM7\DWSIM.Automation.dll
  (Update the path inside run_screening.py if different)

Install dependencies:
pip install -r requirements.txt


## 3. Usage
Run the main script:
python run_screening.py


This produces:
results.csv
plots/ (optional)


## 4. Output
results.csv includes:
- Metadata
- Sweep parameters
- Conversion, outlet flows, heat duties
- Distillate purity, bottom purity
- Condenser & reboiler duties
- Error handling flags

## 5. Notes
- All flowsheets are built programmatically.
- No GUI interaction occurs.
- Script handles errors gracefully.