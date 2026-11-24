#car form to car rent and buy 
class Car:
     

    def __init__(self, make:str, model:str, year:int, price:int, car_plate:str, color:str, status:bool  ):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.car_plate = car_plate
        self.color = color
        self.status = status

    def display_info(self):
        print(f"Car Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.price}")
        print(f"Car Plate: {self.car_plate}")  
        print(f"Color: {self.color}")
        print(f"Status: {'Available' if self.status else 'Not Available'}")
        
 #test 
 
car1 = Car("Toyota", "Camry", 2020, 25000, "ABC123", "Blue", True)
car1.display_info()
 