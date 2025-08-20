from __future__ import annotations

from typing import Dict, Iterable, Final

from .sensor import Sensor

# Health formula constants
BASE_HEALTH: Final[float] = 100.0
TEMP_DIVISOR: Final[float] = 2.0
PRESSURE_DIVISOR: Final[float] = 10.0
VIBRATION_MULTIPLIER: Final[float] = 20.0


class Machine:
    """Stores sensors and computes an overall health score.

    health = 100 - (temp/2 + pressure/10 + vibration*20)
    If any of the three sensors is missing → "Sensor Offline Warning".
    """

    def __init__(self, machine_id: str) -> None:
        self._id = str(machine_id)
        self._sensors_by_type: Dict[str, Sensor] = {}

    @property
    def id(self) -> str:
        return self._id

    def add_sensor(self, sensor: Sensor) -> None:
        # Last sensor of a given type wins
        self._sensors_by_type[sensor.type] = sensor

    def _get_reading_or_none(self, sensor_type: str) -> float | None:
        sensor = self._sensors_by_type.get(sensor_type)
        return sensor.reading if sensor is not None else None

    def compute_health(self) -> float | str:
        temp = self._get_reading_or_none("Temperature")
        pressure = self._get_reading_or_none("Pressure")
        vibration = self._get_reading_or_none("Vibration")

        missing_any = temp is None or pressure is None or vibration is None

        if missing_any:
            return "Sensor Offline Warning"

        health = BASE_HEALTH - (
            temp / TEMP_DIVISOR + pressure / PRESSURE_DIVISOR + vibration * VIBRATION_MULTIPLIER
        )
        return health

