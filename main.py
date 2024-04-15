from ElevatorControlSystem import ElevatorControlSystem
from Floor import Floor
from State import State
import Elevator
def main():
    # Initialize the elevator system with 2 elevators
    total_floors = 5
    ecs = ElevatorControlSystem(total_floors)

    while True:
        floor = int(input("Please enter the destination floor: "))
        
     
        if floor>total_floors:
            print("Sorry, invalid floor number, please enter a valid floor number: ")
            continue

        current_floor = Floor(floor)
        
        print("*"*50)
        # Simulate floor requests
        print("Floor %d calls an elevator."%(floor))
        current_floor.call_elevator()
        ecs.request_elevator(current_floor.floor_number)
        print("*"*50)
        

    
if __name__ == "__main__":
    main()
