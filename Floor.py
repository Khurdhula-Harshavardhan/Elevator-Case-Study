class Button:
    def __init__(self, floor):
        """
        Initialize the button with the floor number it represents.
        
        :param floor: int - The floor number this button is associated with.
        """
        self.floor = floor
        self.is_pressed = False

    def press_button(self):
        """
        Simulate pressing the button. This changes the button's state to pressed.
        """
        self.is_pressed = True
        print(f"Button for floor {self.floor} pressed.")

    def reset_button(self):
        """
        Reset the button's state to not pressed after the elevator has responded to the request.
        """
        self.is_pressed = False
        print(f"Button for floor {self.floor} reset.")
