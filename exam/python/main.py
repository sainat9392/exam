from __future__ import annotations

import csv
import os
import sys
from typing import Dict

from .factory_monitor import FactoryMonitor
from .machine import Machine
from .sensor import Sensor


REQUIRED_COLUMNS = ("machine_id", "sensor_id", "sensor_type", "reading")


def load_machines_from_csv(csv_path: str) -> Dict[str, Machine]:
    if not os.path.exists(csv_path):
        raise ValueError(f"CSV file not found: {csv_path}")

    with open(csv_path, newline="", encoding="utf-8") as f:
        try:
            reader = csv.DictReader(f)
        except Exception as exc:  # pragma: no cover - very unlikely
            raise ValueError(f"Malformed CSV: {exc}") from exc

        if reader.fieldnames is None:
            raise ValueError("Malformed CSV: missing header")

        missing_cols = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing_cols:
            raise ValueError(f"Malformed CSV: missing columns {missing_cols}")

        machines: Dict[str, Machine] = {}
        row_count = 0
        for row in reader:
            row_count += 1
            machine_id = (row.get("machine_id") or "").strip()
            sensor_id = (row.get("sensor_id") or "").strip()
            sensor_type = (row.get("sensor_type") or "").strip()
            reading_str = (row.get("reading") or "").strip()

            if not machine_id or not sensor_id or not sensor_type or not reading_str:
                raise ValueError("Malformed CSV: empty fields present")

            try:
                reading = float(reading_str)
            except ValueError as exc:
                raise ValueError(f"Malformed CSV: non-numeric reading '{reading_str}'") from exc

            if machine_id not in machines:
                machines[machine_id] = Machine(machine_id)
            machines[machine_id].add_sensor(Sensor(sensor_id, sensor_type, reading))

        if row_count == 0:
            raise ValueError("Empty CSV: no data rows found")

        return machines


def main() -> None:
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "data.csv"
    machines = load_machines_from_csv(csv_path)
    monitor = FactoryMonitor(machines.values())
    monitor.check_health()


if __name__ == "__main__":
    main()

