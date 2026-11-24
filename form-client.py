#client form to car rent and buy 
class Client: 

    def __init__(self, name:str, email:str, phone:str, address:str):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

    def display_info(self):
        print(f"Client Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}") 
        
        
#test

client1 = Client("John Doe", "john.doe@example.com", "123-456-7890", "123 Main St")
client1.display_info()
        