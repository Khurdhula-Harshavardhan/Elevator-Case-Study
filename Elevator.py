from State import State

class Elevator:
    def __init__(self, current_floor):
        self.current_floor = current_floor
        self.state = State.IDLE

    def move_to_floor(self, target_floor):
        print(f"Moving from floor {self.current_floor} to floor {target_floor}")
        self.current_floor = target_floor
        self.state = State.MOVING
        print(f"Elevator has arrived at floor {target_floor}")
        self.state = State.IDLE
