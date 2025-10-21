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
h = Elevator(1, 10)
print("Basic elevator test:")
h.go_to_floor(5)
h.go_to_floor(1)