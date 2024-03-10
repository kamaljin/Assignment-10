class Elevator:
    def __init__(self, bottom, top):
        self.current_floor = bottom
        self.bottom_floor = bottom
        self.top_floor = top

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            self.floor_up(floor)
        elif floor < self.current_floor:
            self.floor_down(floor)

    def floor_up(self, floor):
        while self.current_floor < floor:
            self.current_floor += 1
            print("Elevator reached floor", self.current_floor)

    def floor_down(self, floor):
        while self.current_floor > floor:
            self.current_floor -= 1
            print("Elevator reached floor", self.current_floor)

elevator = Elevator(1, 10)
elevator.go_to_floor(5)
elevator.go_to_floor(1)
