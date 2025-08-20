from __future__ import annotations

from typing import Final


ALLOWED_SENSOR_TYPES: Final[set[str]] = {"Temperature", "Pressure", "Vibration"}


class Sensor:
    """Represents a single sensor with an id, type, and numeric reading.

    Only the types in ALLOWED_SENSOR_TYPES are permitted.
    """

    def __init__(self, sensor_id: str, sensor_type: str, reading: float) -> None:
        if sensor_type not in ALLOWED_SENSOR_TYPES:
            raise ValueError(
                f"Invalid sensor type '{sensor_type}'. Allowed: {sorted(ALLOWED_SENSOR_TYPES)}"
            )
        self._id = str(sensor_id)
        self._type = sensor_type
        self._reading = float(reading)

    @property
    def id(self) -> str:
        return self._id

    @property
    def type(self) -> str:
        return self._type

    @property
    def reading(self) -> float:
        return self._reading

    def __repr__(self) -> str:  # Helpful for debugging/logging
        return f"Sensor(id={self._id!r}, type={self._type!r}, reading={self._reading!r})"

