from ElevatorControlSystem import ElevatorControlSystem
from Floor import Floor
from State import State
def main():
    # Initialize the elevator system with 2 elevators
    ecs = ElevatorControlSystem(2)
    
    # Create floors
    floor1 = Floor(1)
    floor2 = Floor(2)

    # Simulate floor requests
    print("Floor 1 calls an elevator.")
    floor1.call_elevator()
    ecs.request_elevator(floor1.floor_number)

    print("\nFloor 2 calls an elevator.")
    floor2.call_elevator()
    ecs.request_elevator(floor2.floor_number)

if __name__ == "__main__":
    main()
