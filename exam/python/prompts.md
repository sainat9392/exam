
Sensor Class
Write a Python class Sensor with attributes: id, type, and reading.
Allowed types: "Temperature", "Pressure", "Vibration".
Example:
Input → Sensor("S1", "Temperature", 95)
Output → prints "Sensor S1: Temperature = 95"

Machine Health Calculator
Create a Machine class that stores multiple sensors.
Formula: health = 100 - (temp/2 + pressure/10 + vibration*20)
Example:
Input → Machine with Temperature=120, Pressure=250, Vibration=1.5
Output → "Health = 37.5, Alert: Critical Machine Failure Risk"

Factory Monitor with Multiple Machines
Build a FactoryMonitor class that manages many Machine objects.
It should compute the average health of all machines and detect anomalies.
Example:
Input → Machine1(health=60), Machine2(health=30)
Output → "Average Factory Health = 45"

CSV Data Loader
Write a program that loads machine sensor data from a CSV file.
Format:
Machine1, Temperature, 95
Machine1, Pressure, 220
Machine2, Vibration, 0.7
Output → print health of each machine with alerts.

Sensor Offline Warning
Modify the Machine class to raise a warning if any sensor is missing.
Example:
Input → Machine with only Temperature=90
Output → "Sensor Offline Warning"

Concurrency Simulation
Use threading.Thread to simulate real-time sensor updates.
Use threading.Lock for safe updates when multiple threads run.
Example:
Input → 5 machines updating sensors in parallel
Output → print updated health scores continuously.
