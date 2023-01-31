class Car():
    def __init__(self, currentSpeed, maxSpeed,fuelLevel, colour):
        self.currentSpeed = currentSpeed
        self.maxSpeed = maxSpeed
        self.fuelLevel = fuelLevel
        self.colour = colour

    def accelerate(self, speed):
        self.currentSpeed + speed
        self.fuelLevel - 1

    def brake(self, force):
        self.currentSpeed - force

    def refuel(self):
        self.fuelLevel - 1