class Car:
    def __init__(self, license_plate, maximum_speed):
        self.hours = None
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, changed_speed):
        self.current_speed = self.current_speed + changed_speed
        if self.current_speed < 0:
            self.current_speed = 0
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def drive(self, hours):
        self.hours = hours
        self.travelled_distance = self.current_speed * self.hours + self.travelled_distance

import random
class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            random_acceleration = random.randint(-10, 15)
            car.accelerate(random_acceleration)
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(f"The car: {car.license_plate} drives at speed {car.maximum_speed} km/h, has made already {car.travelled_distance} km.")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
            else:
                return False



cars = []
for i in range(10):
    car = Car(f"ABC-{i+1}", random.randint(100, 200))
    cars.append(car)

race = Race("Grand Demolition Derby", 8000, cars)
print(f"Race created: {race.name} ({race.distance} km)")
print(f"Cars participating: {len(race.cars)}")

print(f"\nRace finished initially: {race.race_finished()}")

for hour in range(5):
    race.hour_passes()
    if hour == 2:
        print(f"After {hour+1} hours, race finished: {race.race_finished()}")