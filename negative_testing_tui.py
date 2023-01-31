import pytest
from tui import Car

def test_Car_Colour_failed():
    mclaren = Car(0, 0, 0, "Black")
    assert not mclaren.colour == "Yellow"

def test_Car_currentSpeed():
    mclaren = Car(0, 0, 0, "Black")
    assert mclaren.currentSpeed == 0
