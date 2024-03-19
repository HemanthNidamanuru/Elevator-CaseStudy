class User:
    def _init_(self, current_floor, destination_floor):
        self.current_floor = current_floor
        self.destination_floor = destination_floor

    def press_button(self):
        print(f"User pressed button to go from floor {self.current_floor} to floor {self.destination_floor}")
