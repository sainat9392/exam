from __future__ import annotations

from typing import Iterable, List, Final

from .machine import Machine


class FactoryMonitor:
    """Manages Machine objects and prints health evaluations."""

    def __init__(self, machines: Iterable[Machine]):
        self._machines: List[Machine] = list(machines)

    def check_health(self) -> None:
        CRITICAL_HEALTH_THRESHOLD: Final[float] = 50.0
        for machine in self._machines:
            health_or_warning = machine.compute_health()
            if isinstance(health_or_warning, str):
                print(f"Machine {machine.id} Health: {health_or_warning}")
                continue
            print(f"Machine {machine.id} Health: {health_or_warning:.2f}")
            if health_or_warning < CRITICAL_HEALTH_THRESHOLD:
                print("Critical Machine Failure Risk")

