class Button:
    def __init__(self, floor):
        self.floor = floor
        self.is_pressed = False

    def press(self):
        self.is_pressed = True
        print(f"Button for floor {self.floor} has been pressed.")

    def reset(self):
        self.is_pressed = False
        print(f"Button for floor {self.floor} has been reset.")
