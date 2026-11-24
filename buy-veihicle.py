#take the class vendedores.py and import it to this file
#take the class veiculo.py and import it to this file
#take the form-client.py and import it to this file
import importlib.util
from pathlib import Path
from typing import Any, Mapping

import vendedores


def _load_class_from_file(module_name: str, class_name: str, file_name: str):
    module_path = Path(__file__).with_name(file_name)
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load {file_name}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)


Car = _load_class_from_file("car_form", "Car", "car-form.py")
Client = _load_class_from_file("form_client", "Client", "form-client.py")
class BuyVeihicle:
    def __init__(self, client: Any, car: Any, vendedor: Mapping[str, Any], id: int, buy_date: str, price: float, discount: float):
        self.id = id
        self.client = client
        self.car = car
        self.vendedor = vendedor
        self.buy_date = buy_date
        self.price=price
        self.discount=discount

    def display_info(self):
        print(f"Purchase ID: {self.id}")
        print("Client Information:")
        self.client.display_info()
        print("\nCar Information:")
        self.car.display_info()
        print("\nVendedor Information:")
        print(f"Name: {self.vendedor.get('nome', 'N/A')}")
        print(f"CPF: {self.vendedor.get('cpf', 'N/A')}")
        print(f"Phone: {self.vendedor.get('telefone', 'N/A')}")
        print(f"Email: {self.vendedor.get('email', 'N/A')}")
        print(f"Commission: {self.vendedor.get('percentual_comissao', 'N/A')}%")
        print(f"Status: {self.vendedor.get('status', 'N/A')}")
        print(f"\nBuy Date: {self.buy_date}")
        print(f"Price: {self.price}")
        
        
#test
if not vendedores.vendedores:
    raise RuntimeError("Cadastre pelo menos um vendedor antes de registrar uma compra.")

buy_vehicle = BuyVeihicle(
    client=Client("John Doe", "john.doe@example.com", "123-456-7890", "123 Main St"),
    car=Car("Toyota", "Camry", 2020, 25000, "ABC123", "Blue", True),
    vendedor=vendedores.vendedores[0],
    id=1,
    buy_date="2023-10-01",
    price=25000.0,
    discount=0.1
)
buy_vehicle.display_info()