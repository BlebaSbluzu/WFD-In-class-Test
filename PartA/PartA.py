import datetime

class Vehicle():
    def __init__(self,name,year,max_speed,colour,mileage):
        self.name = name
        self.year = year
        self.max_speed = max_speed
        self.colour = colour
        self.mileage = mileage

    def to_string(self):
        print( self.name + " " + str(self.year) + " " + self.colour + " " + str(self.mileage) + " " + str(self.max_speed))

    def set_name(self, name):
        self.name = name

    def set_year(self, year):
        self.year = year

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_colour(self, colour):
        self.colour = colour


class Car(Vehicle):
    lastNCTdate = datetime
    make = ""

    def to_string(self):
        print( self.name + " " + str(self.year) + " " + self.colour + " " + str(self.mileage) + " " + str(self.max_speed) + " " + str(self.lastNCTdate) + " " + self.make)

    def set_lastNCTdate(self, lastNCTdate):
        self.lastNCTdate = lastNCTdate

    def set_make(self, make):
        self.make = make


# # CHILD OF VEHICLE CLASS

my_vehicle = Vehicle("bike",2012, 30, "purple", 100)

my_car = Car("car number 1",1999,300,"red",1000)

my_car.set_make("honda")
my_car.set_lastNCTdate(datetime.datetime(2020,2,4))

my_vehicle.to_string()

my_car.to_string()

my_vehicle.set_mileage(60)
my_car.set_make("bmw")

my_vehicle.to_string()

my_car.to_string()
