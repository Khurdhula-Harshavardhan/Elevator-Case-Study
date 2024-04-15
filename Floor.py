from Button import Button

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.button = Button(floor_number)

    def call_elevator(self):
        self.button.press()
        print(f"Elevator called to floor {self.floor_number}")
