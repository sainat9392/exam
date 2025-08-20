## Factory Monitoring System (Python)

An object-oriented factory monitoring system that models sensors and machines, computes machine health, and prints alerts based on CSV input.

## Project structure
```
python/
  __init__.py
  sensor.py
  machine.py
  factory_monitor.py
  main.py

data.csv  (example input)
```

## Classes

### Sensor (`python/sensor.py`)
- Attributes: `id` (str), `type` (str), `reading` (float)
- Validation: only `Temperature`, `Pressure`, `Vibration` are allowed; otherwise `ValueError`

### Machine (`python/machine.py`)
- Holds: `Sensor` objects (keyed by sensor type)
- Method: `compute_health()` → returns a float health or the string `"Sensor Offline Warning"` if any required sensor is missing
- Formula: `100 - (temp/2 + pressure/10 + vibration*20)`
- Magic numbers are replaced with named constants in the code

### FactoryMonitor (`python/factory_monitor.py`)
- Holds: multiple `Machine` objects
- Method: `check_health()` → prints each machine’s health; if health < 50 prints `"Critical Machine Failure Risk"`

## CSV input
- Required header: `machine_id,sensor_id,sensor_type,reading`
- `sensor_type` must be one of: `Temperature`, `Pressure`, `Vibration`
- Raises `ValueError` for: missing/empty file, missing header/columns, empty fields, non-numeric readings, or no data rows

### Example CSV (`data.csv`)
```
machine_id,sensor_id,sensor_type,reading
M1,S1,Temperature,60
M1,S2,Pressure,100
M1,S3,Vibration,1.5
M2,S4,Temperature,40
M2,S5,Pressure,80
```

### Example output
```
Machine M1 Health: 30.00
Critical Machine Failure Risk
Machine M2 Health: Sensor Offline Warning
```

## Run
From the repo root, run the main module (path defaults to `data.csv` if omitted):
```powershell
python -m python.main data.csv
```
If you see CSV-related errors, check that your file has the required header and valid values.