import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def drive(self, hours):
        self.distance += self.speed * hours

    def __str__(self):
        return f"{self.name} - {self.distance} km"

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.speed += random.randint(-20, 20)
            car.drive(1)

    def print_status(self):
        print(f"Current status of cars in {self.name}:")
        for car in self.cars:
            print(car)
        print()

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False

# Main program
def main():
    cars = [
        Car("Car 1", 100),
        Car("Car 2", 110),
        Car("Car 3", 95),
        Car("Car 4", 105),
        Car("Car 5", 120),
        Car("Car 6", 90),
        Car("Car 7", 115),
        Car("Car 8", 105),
        Car("Car 9", 100),
        Car("Car 10", 110)
    ]

    race = Race("Grand Demolition Derby", 8000, cars)

    while not race.race_finished():
        race.hour_passes()
        if race.race_finished() or race.distance % 10 == 0:
            race.print_status()

    race.print_status()

if __name__ == "__main__":
    main()

