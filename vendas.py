
class VendaVeiculo:

    def __init__(self, cliente, veiculo, placa, valor, cupom):
        self.cliente = cliente
        self.veiculo = veiculo
        self.placa = placa
        self.valor = valor
        self.cupom = cupom
        self.tipo = "Venda"

    def to_dict(self):
        return {
            "cliente": self.cliente,
            "veiculo": self.veiculo,
            "placa": self.placa,
            "valor": self.valor,
            "cupom": self.cupom,
            "tipo": self.tipo
        }
