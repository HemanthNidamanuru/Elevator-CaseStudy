class Elevator:
    def __init__(self, elevator_id, current_floor):
        self._elevator_id = elevator_id
        self._current_floor = current_floor
        self._timeout = 0  # Default timeout value

    @property
    def elevator_id(self):
        return self._elevator_id

    @property
    def current_floor(self):
        return self._current_floor

    @current_floor.setter
    def current_floor(self, value):
        self._current_floor = value

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


class FloorButton:
    def __init__(self, floor_number):
        self._floor_number = floor_number

    @property
    def floor_number(self):
        return self._floor_number

    def press_up(self):
        print(f"Pressed up button on floor {self.floor_number}")

    def press_down(self):
        print(f"Pressed down button on floor {self.floor_number}")


class ElevatorButton:
    def __init__(self, destination_floor):
        self._destination_floor = destination_floor

    @property
    def destination_floor(self):
        return self._destination_floor

    def press(self):
        print(f"Pressed elevator button for floor {self.destination_floor}")


class User:
    def __init__(self, current_floor, destination_floor, controller):
        self._current_floor = current_floor
        self._destination_floor = destination_floor
        self._controller = controller

    @property
    def current_floor(self):
        return self._current_floor

    @property
    def destination_floor(self):
        return self._destination_floor

    def press_button(self):
        print(f"User pressed button to go from floor {self.current_floor} to floor {self.destination_floor}")
        self._controller.assign_elevator(self.current_floor, self.destination_floor)  # Coupling with ElevatorController


class ElevatorController:
    def __init__(self, elevator_list, floor_list):
        self._elevator_list = elevator_list
        self._floor_list = floor_list

    def assign_elevator(self, current_floor, destination_floor):
        print("Elevator assigned and handled")
        # Here you can implement the logic to assign the elevator based on the current and destination floors
        # Refactored to encapsulate the logic of elevator assignment
        # Cohesion: This method encapsulates the logic for assigning an elevator, promoting functional cohesion


# Example Usage
elevator1 = Elevator("E1", 1)
elevator2 = Elevator("E2", 5)

floor_button = FloorButton(3)
floor_button.press_up()  # Coupling with FloorButton

elevator_button = ElevatorButton(7)
elevator_button.press()  # Coupling with ElevatorButton

controller = ElevatorController([elevator1, elevator2], [1, 2, 3, 4, 5, 6, 7])

user = User(3, 7, controller)
user.press_button()  # Coupling with User
