import random

# Base class
class Vehicle:
    def __init__(self, name):
        self.name = name
        self.__speed = 120  # private speed level

    def race(self):
        self.__speed += 20
        print(f"{self.name} got fast speed! Speed is now {self.__speed}.")

    def check_speed(self):
        print(f"{self.name}'s speed is: {self.__speed}")

    def sound(self):
        print(f"{self.name} makes a noise.")  # gets overridden

# Subaru class inherits Vehicle
class Subaru(Vehicle):
    def sound(self):
        print(f"{self.name} says: Tatatatata!")

# Benz class inherits Vehicle
class Benz(Vehicle):
    def sound(self):
        print(f"{self.name} says: Grrrrrrr!")

# Toyota class inherits Vehicle
class Toyota(Vehicle):
    def sound(self):
        print(f"{self.name} says: Rampapaaaaa!")

# --- Mini Game Logic ---
def car_game():
    print("Welcome to the car Simulator!")
    car_type = input("Choose your car (Subaru/Benz/Toyota): ").lower()
    name = input("What is your car's name? ")

    if car_type == "subaru":
        car = Subaru(name)
    elif car_type == "benz":
        car = Benz(name)
    elif car_type == "toyota":
       car = Toyota(name)
    else:
        print("Unknown car type! You get a mystery car.")
        car = Vehicle(name)

    # Interact with the game
    while True:
        print("\nWhat would you like to do?")
        print("1. race")
        print("2. sound")
        print("3. Check speed")
        print("4. Quit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            car.race()
        elif choice == "2":
            car.sound()
        elif choice == "3":
            car.check_speed()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# Run the game
car_game()
