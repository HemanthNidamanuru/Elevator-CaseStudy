class Elevator:
    def _init_(self, elevator_id, current_floor):
        self.elevator_id = elevator_id
        self.current_floor = current_floor
        self.timeout = 0  # Default timeout value

    def open_door(self):
        print(f"Elevator {self.elevator_id} door opened.")

    def close_door(self):
        print(f"Elevator {self.elevator_id} door closed.")

    def move_up(self):
        self.current_floor += 1
        print(f"Elevator {self.elevator_id} moving up to floor {self.current_floor}")

    def move_down(self):
        self.current_floor -= 1
        print(f"Elevator {self.elevator_id} moving down to floor {self.current_floor}")
