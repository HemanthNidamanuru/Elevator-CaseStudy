import time

class Elevator:
    def __init__(self, current_floor=0):
        self.current_floor = current_floor
        self.destination_floor = None

    def move_to_floor(self, floor):
        print(f"Elevator moving from floor {self.current_floor} to floor {floor}")
        time.sleep(abs(floor - self.current_floor) * 0.5)  # Simulating elevator movement time
        self.current_floor = floor
        self.destination_floor = None  # Clear the destination floor after reaching it

    def open_doors(self, floor):
        print(f"Elevator doors opening at floor {floor}...")
        time.sleep(1)

    def close_doors(self, floor):
        print(f"Elevator doors closing at floor {floor}...")
        time.sleep(1)

class User:
    def __init__(self, name, current_floor, destination_floor):
        self.name = name
        self.current_floor = current_floor
        self.destination_floor = destination_floor

    def enter_elevator(self, elevator):
        print(f"{self.name} enters the elevator at floor {self.current_floor}")
        # Wait until the elevator has reached the correct floor
        while elevator.current_floor != self.current_floor:
            time.sleep(0.1)
        # Open the doors once the elevator has reached the correct floor
        elevator.open_doors(self.current_floor)
        elevator.close_doors(self.current_floor)

    def exit_elevator(self, elevator):
        print(f"{self.name} exits the elevator at floor {self.destination_floor}")
        elevator.open_doors(self.destination_floor)
        elevator.close_doors(self.destination_floor)

def main():
    elevator = Elevator()
    print("Elevator initialized at floor 0")

    user_a_floor = int(input("Enter User A's current floor: "))
    user_a_destination = int(input("Enter User A's destination floor: "))
    user_a = User("User A", user_a_floor, user_a_destination)

    user_b_floor = int(input("Enter User B's current floor: "))
    user_b_destination = int(input("Enter User B's destination floor: "))
    user_b = User("User B", user_b_floor, user_b_destination)

    # Find the nearest floor to pick up or drop off passengers
    nearest_floor = min(user_a_floor, user_b_floor)

    # Elevator actions
    if user_a_floor != user_a_destination or user_b_floor != user_b_destination:
        elevator.move_to_floor(nearest_floor)
        if user_a_floor != user_a_destination:
            if elevator.current_floor == user_a_floor:
                user_a.enter_elevator(elevator)
            elevator.move_to_floor(user_a_destination)
            user_a.exit_elevator(elevator)
        if user_b_floor != user_b_destination:
            if elevator.current_floor == user_b_floor:
                user_b.enter_elevator(elevator)
            else:  # Check if elevator is already at user B's current floor
                elevator.move_to_floor(user_b_floor)
                user_b.enter_elevator(elevator)
            elevator.move_to_floor(user_b_destination)
            user_b.exit_elevator(elevator)

if __name__ == "__main__":
    main()
