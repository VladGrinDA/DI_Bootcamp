class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")


class Car(Vehicle):
    def __init__(self, make, model, number_of_doors):
        super().__init__(make, model)
        self.number_of_doors = number_of_doors

    def open_trunk(self):
        print(f"Opening the trunk of the {self.make} {self.model}.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, has_sidecar=False):
        super().__init__(make, model)
        self.has_sidecar = has_sidecar

    def pop_wheelie(self):
        print(f"{self.make} {self.model} is popping a wheelie!")


# Create a Car instance
my_car = Car("Toyota", "Corolla", 4)
my_car.start()
my_car.open_trunk()
my_car.stop()

# Create a Motorcycle instance
my_motorcycle = Motorcycle("Harley-Davidson", "Street 750")
my_motorcycle.start()
my_motorcycle.pop_wheelie()
my_motorcycle.stop()
