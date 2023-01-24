from tui import Car

pikatchu = Car(0,0,0,"Black")
babyGoat = Car(1,1,1,"Baby Blue")

print(f"The first car current speed of the car is {pikatchu.currentSpeed}, the max speed is {pikatchu.maxSpeed}, the fuel level is {pikatchu.fuelLevel} and the color of it is {pikatchu.colour}")

print(f"\nThe second car current speed of the car is {babyGoat.currentSpeed}, the max speed is {babyGoat.maxSpeed}, the fuel level is {babyGoat.fuelLevel} and the color of it is {babyGoat.colour}")

pikatchu.accelerate(5)
print(f"\nThe first car is now on the motorway so the speed current speed is {pikatchu.currentSpeed}")
babyGoat.brake(3)

print(f"\nThe second car is now approaching the motorway but has to brake as there is traffic so its current speed is {babyGoat.currentSpeed}")
