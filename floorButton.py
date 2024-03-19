class FloorButton:
    def _init_(self, floor_number):
        self.floor_number = floor_number

    def press_up(self):
        print(f"Pressed up button on floor {self.floor_number}")

    def press_down(self):
        print(f"Pressed down button on floor {self.floor_number}")
