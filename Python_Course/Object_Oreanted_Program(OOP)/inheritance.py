class Vechile:
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self._year = year

    # getter and setter for brand
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        self._brand = brand

    # getter and setter for model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        self._model = model

    # getter and setter for year
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        self._year = year

    # action/behavoiur
    def start_engine(self):
        return f"{self._brand} {self._model} engine started"
        
    def __str__(self):
        return f"Vechile: {self._brand} {self._model} {self._year} "

class Car(Vechile):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self._doors = doors

    def open_trunk(self):
        return f"{self._brand} {self._model} {self._doors}'s has open."

    @property
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, doors):
        self._doors = doors    
    
class Bike(Vechile):
    def __init__(self, brand, model, year, cc):
        super().__init__(brand, model, year)
        self._cc = cc

    def wheelie(self):
        return f"{self._brand} {self._model} perform a wheelie!"

    @property
    def cc(self):
        return self._cc
    
    @cc.setter
    def cc(self, cc):
        self._cc = cc

class Truck(Vechile):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self._capacity = capacity

    def load_cargo(self):
        return f"{self._model} is loading {self._capacity} tons of cargo."
    
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

# instances:
car1 = Car("Supra", "Grx5", 1990, "Carbon fider")
bike1 = Bike("Duke", "500", 2000, 500)
truck1 = Truck("Honda", "Rxp2", 2020, "40T")

# calling methods of instance Car
print(car1.open_trunk())
print(car1.start_engine())
print(car1)

# calling methods of instance Bike
print(bike1.start_engine())
print(bike1.wheelie())
print(bike1)

# calling methods of instance Truck
print(truck1.load_cargo())
print(truck1.start_engine())
print(truck1)

# getting few attributes for instances:
print(car1.brand)
print(bike1.model)
print(truck1.year)
print(car1.doors)
print(bike1.cc)
print(truck1.load_cargo)

# changing few attributes of instances:
car1.brand = "Bugati"
bike1.model= "Fx09"
truck1.year = 1993
car1.doors = 5
bike1.cc = 950
truck1.capacity = "15T"

# calling the changed attributes:
print(car1.brand)
print(bike1.model)
print(truck1.year)
print(car1.doors)
print(bike1.cc)
print(truck1.capacity)