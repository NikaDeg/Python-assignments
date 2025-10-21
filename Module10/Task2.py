class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor + 1 >= self.top_floor:
            self.current_floor = self.top_floor
        else:
            self.current_floor += 1
        print(f"Elevator is at {self.current_floor} floor.")

    def floor_down(self):
        if self.current_floor - 1 <= self.bottom_floor:
            self.current_floor = self.bottom_floor
        else:
            self.current_floor -= 1
        print(f"Elevator is at {self.current_floor} floor.")

    def go_to_floor(self, floor):
        if floor < self.current_floor:
            while self.current_floor != floor:
                self.floor_down()
        if floor > self.current_floor:
            while self.current_floor != floor:
                self.floor_up()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(number_of_elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, elevator_number, floor):
        self.elevators[elevator_number].go_to_floor(floor)


# # Test Building with multiple elevators
# building = Building(1, 10, 3)
# building.run_elevator(0, 5)
# building.run_elevator(1, 3)
# building.run_elevator(2, 8)
#
# # Test single elevator building
# small_building = Building(0, 5, 1)
# small_building.run_elevator(0, 4)
#
# # Test larger building
# office = Building(1, 6, 5)
# office.run_elevator(0, 4)
# office.run_elevator(4, 2)