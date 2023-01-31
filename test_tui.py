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



