class ElevatorController:
    def _init_(self, elevator_list, floor_list):
        self.elevator_list = elevator_list
        self.floor_list = floor_list

    def assign_elevator(self):
        print("Elevator assigned and handled")
