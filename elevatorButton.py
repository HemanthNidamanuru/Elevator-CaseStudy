class ElevatorButton:
    def _init_(self, destination_floor):
        self.destination_floor = destination_floor

    def press(self):
        print(f"Pressed elevator button for floor {self.destination_floor}")
