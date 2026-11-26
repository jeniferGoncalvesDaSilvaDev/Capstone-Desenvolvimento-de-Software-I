
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vendas import VendaVeiculo

app = FastAPI(title="Katchau - Venda de Veículos")

vendas = []


class VendaRequest(BaseModel):
    cliente: str
    veiculo: str
    placa: str
    valor: float
    cupom: str = ""


@app.get("/")
def inicio():
    return {"mensagem": "API Katchau funcionando!"}


@app.post("/vendas")
def registrar_venda(dados: VendaRequest):

    if not dados.cliente.strip():
        raise HTTPException(
            status_code=400,
            detail="Informe o nome do cliente."
        )

    if not dados.veiculo.strip():
        raise HTTPException(
            status_code=400,
            detail="Informe o modelo do veículo."
        )

    if not dados.placa.strip():
        raise HTTPException(
            status_code=400,
            detail="Informe a placa do veículo."
        )

    if dados.valor <= 0:
        raise HTTPException(
            status_code=400,
            detail="O valor deve ser maior que zero."
        )

    nova_venda = VendaVeiculo(
        dados.cliente,
        dados.veiculo,
        dados.placa,
        dados.valor,
        dados.cupom
    )

    vendas.append(nova_venda.to_dict())

    return {
        "mensagem": "Venda registrada com sucesso!",
        "venda": nova_venda.to_dict()
    }


@app.get("/vendas")
def listar_vendas():
    return vendas


@app.get("/vendas/{placa}")
def consultar_venda(placa: str):

    resultado = [
        venda for venda in vendas
        if venda["placa"].upper() == placa.upper()
    ]

    if not resultado:
        raise HTTPException(
            status_code=404,
            detail="Venda não encontrada."
        )

    return resultado
