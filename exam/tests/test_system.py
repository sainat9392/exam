import io
from contextlib import redirect_stdout

import pytest

from python.sensor import Sensor
from python.machine import Machine
from python.factory_monitor import FactoryMonitor
from python.main import load_machines_from_csv


def test_critical_alert_when_health_below_50(capsys):
    m = Machine("M1")
    m.add_sensor(Sensor("S1", "Temperature", 120))
    m.add_sensor(Sensor("S2", "Pressure", 250))
    m.add_sensor(Sensor("S3", "Vibration", 1.5))

    fm = FactoryMonitor([m])
    fm.check_health()
    captured = capsys.readouterr().out
    assert "Critical Machine Failure Risk" in captured


def test_missing_sensor_warning(capsys):
    m = Machine("M2")
    m.add_sensor(Sensor("S1", "Temperature", 40))
    m.add_sensor(Sensor("S2", "Pressure", 80))
    # Missing Vibration

    # Direct compute
    result = m.compute_health()
    assert isinstance(result, str)
    assert result == "Sensor Offline Warning"

    # Via monitor printing
    fm = FactoryMonitor([m])
    fm.check_health()
    captured = capsys.readouterr().out
    assert "Sensor Offline Warning" in captured


def test_factory_average_health():
    # Machine A → health 60: temp=20 (10), pressure=100 (10), vibration=1 (20)
    m1 = Machine("A")
    m1.add_sensor(Sensor("T1", "Temperature", 20))
    m1.add_sensor(Sensor("P1", "Pressure", 100))
    m1.add_sensor(Sensor("V1", "Vibration", 1.0))

    # Machine B → health 30: temp=40 (20), pressure=200 (20), vibration=1.5 (30)
    m2 = Machine("B")
    m2.add_sensor(Sensor("T2", "Temperature", 40))
    m2.add_sensor(Sensor("P2", "Pressure", 200))
    m2.add_sensor(Sensor("V2", "Vibration", 1.5))

    h1 = m1.compute_health()
    h2 = m2.compute_health()
    assert isinstance(h1, float) and isinstance(h2, float)
    avg = (h1 + h2) / 2
    assert pytest.approx(avg, rel=1e-9) == 45.0


def test_boundary_health_equal_50_no_alert(capsys):
    # health = 50 when temp=20 (10) + pressure=100 (10) + vibration=1.5 (30) → sum 50
    m = Machine("M50")
    m.add_sensor(Sensor("S1", "Temperature", 20))
    m.add_sensor(Sensor("S2", "Pressure", 100))
    m.add_sensor(Sensor("S3", "Vibration", 1.5))

    fm = FactoryMonitor([m])
    fm.check_health()
    out = capsys.readouterr().out
    assert "Machine M50 Health: 50.00" in out
    assert "Critical Machine Failure Risk" not in out


def test_empty_csv_raises_value_error(tmp_path):
    empty_csv = tmp_path / "empty.csv"
    empty_csv.write_text("")
    with pytest.raises(ValueError):
        load_machines_from_csv(str(empty_csv))

