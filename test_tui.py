import pytest
from tui import Car

def test_Car_Colour():
    mclaren = Car(0, 0, 0, "Black")
    assert mclaren.colour == "Black"

def test_Car_currentSpeed():
    mclaren = Car(0, 0, 0, "Black")
    assert mclaren.currentSpeed == 0

def test_Car_maxSpeed():
    mclaren = Car(0, 0, 0, "Black")
    assert mclaren.maxSpeed == 0

def test_Car_fuelLevel():
    mclaren = Car(0, 0, 0, "Black")
    assert mclaren.fuelLevel == 0

def test_currentSpeed_accelerate_changes():
    mclaren = Car(0, 0, 0, "Black")
    mclaren.accelerate(5)
    assert mclaren.currentSpeed == 5

def test_fuelLevel_accelerate_changes():
    mclaren = Car(10, 9, 8, "Black")
    mclaren.accelerate(5)
    assert mclaren.fuelLevel == 7
def test_currentSpeed_brake_changes():
    mclaren = Car(10, 9, 9, "Black")
    mclaren.brake(5)
    assert mclaren.currentSpeed == 5

def test_refuel_changes():
    mclaren = Car(10, 9, 9, "Black")
    mclaren.refuel()
    assert mclaren.fuelLevel == 10


