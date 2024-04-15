from Elevator import Elevator

class ElevatorControlSystem:
    def __init__(self, number_of_elevators):
        self.elevators = [Elevator(1) for _ in range(number_of_elevators)]

    def request_elevator(self, floor):
        # This is a simple approach; in reality, you'd want to select the closest idle elevator.
        for elevator in self.elevators:
            if elevator.state == State.IDLE:
                elevator.move_to_floor(floor)
                return elevator
        print("All elevators are currently busy.")
