from datetime import datetime, timedelta
import sys

class CarAlreadyExists(Exception):
    pass

class CarNotFound(Exception):
    pass

class ParkingFull(Exception):
    pass

def parse_time(hhmm):
    hh, mm = map(int, hhmm.split(':'))
    return hh * 60 + mm

class Car:
    def __init__(self, plate, owner, entry_time):
        self.plate = plate
        self.owner = owner
        self.entry_time = entry_time 
class ParkingLot:
    def __init__(self, floors, spots_per_floor):
        self.floors = floors
        self.spots_per_floor = spots_per_floor
        self.slots = [[None for _ in range(spots_per_floor)] for _ in range(floors)]
        self.plate_location = {}  
        
    def park(self, plate, owner, time_str):
        if plate in self.plate_location:
            raise CarAlreadyExists()

        for f in range(self.floors):
            for s in range(self.spots_per_floor):
                if self.slots[f][s] is None:
                    car = Car(plate, owner, parse_time(time_str))
                    self.slots[f][s] = car
                    self.plate_location[plate] = (f, s)
                    print(f"Parked at floor {f}, spot {s}")
                    return
        raise ParkingFull()

    def remove(self, plate, time_str):
        if plate not in self.plate_location:
            raise CarNotFound()

        f, s = self.plate_location[plate]
        car = self.slots[f][s]
        exit_time = parse_time(time_str)
        duration = exit_time - car.entry_time
        print(f"Removed from floor {f}, spot {s} after {duration} minutes")
        self.slots[f][s] = None
        del self.plate_location[plate]

    def find(self, plate):
        if plate not in self.plate_location:
            raise CarNotFound()
        f, s = self.plate_location[plate]
        print(f"Found at floor {f}, spot {s}")

def main():
    f_s_line = ''
    while not f_s_line.strip():
        f_s_line = input()
    f, s = map(int, f_s_line.strip().split())
    parking = ParkingLot(f, s)

    while True:
        try:
            line = ''
            while not line.strip():
                line = input()
            parts = line.strip().split()
            if not parts:
                continue
            command = parts[0].lower()

            if command == 'end':
                break
            elif command == 'park':
                plate = parts[1]
                owner = parts[2]
                time_str = parts[3]
                try:
                    parking.park(plate, owner, time_str)
                except CarAlreadyExists:
                    print("Car Already Exists")
                except ParkingFull:
                    print("Parking Full")
            elif command == 'remove':
                plate = parts[1]
                time_str = parts[2]
                try:
                    parking.remove(plate, time_str)
                except CarNotFound:
                    print("Car Not Found")
            elif command == 'find':
                plate = parts[1]
                try:
                    parking.find(plate)
                except CarNotFound:
                    print("Car Not Found")
        except EOFError:
            break

if __name__ == "__main__":
    main()
