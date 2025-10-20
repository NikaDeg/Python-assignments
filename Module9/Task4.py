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
def race():
    cars = []
    for i in range(10):
        random_speed = random.randint(100, 200)
        car = Car(f"ABC-{i+1}", random_speed)
        cars.append(car)
    racing = True
    while racing:
        # check if end race
        for car in cars:
            if car.travelled_distance >= 10000:
                racing = False
        # do race
        for car in cars:
            random_acceleration = random.randint(-10, 15)
            car.accelerate(random_acceleration)
            car.drive(1)

    cars_desc = sorted(cars, key=lambda car: car.travelled_distance, reverse=True)

    return cars_desc

cars = race()
for car in cars:
    print(car.license_plate, car.maximum_speed, car.travelled_distance)

# race_results = race()
# print(f"Race completed! {len(race_results)} cars participated.")
# print("Top 3 finishers:")
# for i, car in enumerate(race_results[:3]):
#     print(f"{i+1}. {car.license_plate}: {car.travelled_distance:.1f} km (speed: {car.current_speed} km/h)")
#
# winner = race_results[0]
# print(f"\nWinner: {winner.license_plate} with {winner.travelled_distance:.1f} km!")