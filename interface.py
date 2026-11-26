
import customtkinter as ctk
import requests
from tkinter import messagebox

API_URL = "http://127.0.0.1:8000"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


def consultar_historico():

    try:
        resposta = requests.get(
            f"{API_URL}/vendas",
            timeout=10
        )

        resposta.raise_for_status()
        lista_vendas = resposta.json()

        janela = ctk.CTkToplevel(app)
        janela.title("Katchau - Histórico")
        janela.geometry("750x520")
        janela.configure(fg_color="#1E1E1E")

        titulo = ctk.CTkLabel(
            janela,
            text="HISTÓRICO DE VENDAS",
            font=("Arial", 24, "bold"),
            text_color="#FFFFFF"
        )
        titulo.pack(pady=20)

        texto = ctk.CTkTextbox(
            janela,
            width=680,
            height=400,
            font=("Arial", 14)
        )
        texto.pack(padx=20, pady=10)

        if not lista_vendas:
            texto.insert("end", "Nenhuma venda registrada.")
        else:
            for venda in lista_vendas:
                texto.insert(
                    "end",
                    f"Cliente: {venda['cliente']}\n"
                    f"Veículo: {venda['veiculo']}\n"
                    f"Placa: {venda['placa']}\n"
                    f"Valor: R$ {venda['valor']:.2f}\n"
                    f"Cupom: {venda['cupom'] or 'Não informado'}\n"
                    "----------------------------------------\n"
                )

        texto.configure(state="disabled")

    except requests.exceptions.RequestException as erro:
        print("Erro ao consultar API:", erro)

        messagebox.showerror(
            "Erro",
            "Não foi possível consultar a API FastAPI."
        )


def abrir_venda():

    janela = ctk.CTkToplevel(app)
    janela.title("Katchau - Vender Veículo")
    janela.geometry("500x600")
    janela.configure(fg_color="#1E1E1E")
    janela.grab_set()

    titulo = ctk.CTkLabel(
        janela,
        text="VENDER VEÍCULO",
        font=("Arial", 24, "bold"),
        text_color="#FFFFFF"
    )
    titulo.pack(pady=25)

    campos = {}

    dados_campos = [
        ("Nome do cliente", "cliente"),
        ("Modelo do veículo", "veiculo"),
        ("Placa", "placa"),
        ("Valor (R$)", "valor"),
        ("Cupom de desconto", "cupom")
    ]

    for rotulo, chave in dados_campos:

        campo_label = ctk.CTkLabel(
            janela,
            text=rotulo,
            font=("Arial", 14),
            text_color="#FFFFFF"
        )
        campo_label.pack(pady=(10, 2))

        campo = ctk.CTkEntry(
            janela,
            width=350,
            height=40,
            placeholder_text=rotulo
        )
        campo.pack()

        campos[chave] = campo

    def registrar():

        cliente = campos["cliente"].get().strip()
        veiculo = campos["veiculo"].get().strip()
        placa = campos["placa"].get().strip()
        valor_texto = campos["valor"].get().strip()
        cupom = campos["cupom"].get().strip()

        if not cliente or not veiculo or not placa or not valor_texto:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos obrigatórios."
            )
            return

        try:
            valor = float(
                valor_texto.replace(".", "").replace(",", ".")
            )
        except ValueError:
            messagebox.showerror(
                "Erro",
                "Informe um valor numérico válido."
            )
            return

        dados = {
            "cliente": cliente,
            "veiculo": veiculo,
            "placa": placa,
            "valor": valor,
            "cupom": cupom
        }

        try:
            resposta = requests.post(
                f"{API_URL}/vendas",
                json=dados,
                timeout=10
            )

            resposta.raise_for_status()

            resultado = resposta.json()

            messagebox.showinfo(
                "Sucesso",
                resultado["mensagem"]
            )

            janela.destroy()

        except requests.exceptions.HTTPError as erro:
            try:
                mensagem = resposta.json().get(
                    "detail",
                    "Não foi possível registrar a venda."
                )
            except ValueError:
                mensagem = "Erro ao processar a resposta da API."

            messagebox.showerror("Erro", mensagem)

        except requests.exceptions.RequestException as erro:
            print("Erro de conexão:", erro)

            messagebox.showerror(
                "Erro",
                "Não foi possível conectar à API FastAPI."
            )

    botao = ctk.CTkButton(
        janela,
        text="REGISTRAR VENDA",
        width=350,
        height=45,
        fg_color="#C62828",
        hover_color="#8E0000",
        font=("Arial", 15, "bold"),
        command=registrar
    )
    botao.pack(pady=30)


# JANELA PRINCIPAL

app = ctk.CTk()

app.title("Katchau - Compra e Venda")
app.geometry("1000x620")
app.configure(fg_color="#1E1E1E")

# MENU LATERAL

menu = ctk.CTkFrame(
    app,
    width=220,
    fg_color="#151515",
    corner_radius=0
)
menu.pack(side="left", fill="y")

logo = ctk.CTkLabel(
    menu,
    text="KATCHAU",
    font=("Arial", 28, "bold"),
    text_color="#C62828"
)
logo.pack(pady=30)

opcoes = [
    "Início",
    "Clientes",
    "Vendedores",
    "Veículos",
    "Aluguel",
    "Venda de Veículos",
    "Comissões",
    "Histórico"
]

for opcao in opcoes:

    if opcao == "Venda de Veículos":
        comando = abrir_venda

    elif opcao == "Histórico":
        comando = consultar_historico

    else:
        comando = lambda nome=opcao: messagebox.showinfo(
            "Katchau",
            f"A seção {nome} ainda não foi implementada."
        )

    botao_menu = ctk.CTkButton(
        menu,
        text=opcao,
        width=190,
        height=40,
        fg_color="transparent",
        hover_color="#333333",
        text_color="#FFFFFF",
        anchor="w",
        command=comando
    )
    botao_menu.pack(pady=5, padx=10)


# ÁREA PRINCIPAL

conteudo = ctk.CTkFrame(
    app,
    fg_color="#1E1E1E"
)
conteudo.pack(
    side="right",
    expand=True,
    fill="both",
    padx=30,
    pady=30
)

titulo = ctk.CTkLabel(
    conteudo,
    text="COMPRA E VENDA DE VEÍCULOS",
    font=("Arial", 28, "bold"),
    text_color="#FFFFFF"
)
titulo.pack(pady=40)

subtitulo = ctk.CTkLabel(
    conteudo,
    text="Gerencie as vendas de veículos pelo sistema Katchau.",
    font=("Arial", 15),
    text_color="#BBBBBB"
)
subtitulo.pack(pady=10)

card = ctk.CTkFrame(
    conteudo,
    width=400,
    height=220,
    fg_color="#292929",
    corner_radius=15
)
card.pack(pady=35)
card.pack_propagate(False)

titulo_card = ctk.CTkLabel(
    card,
    text="VENDER VEÍCULO",
    font=("Arial", 22, "bold"),
    text_color="#FFFFFF"
)
titulo_card.pack(pady=35)

botao_venda = ctk.CTkButton(
    card,
    text="REGISTRAR VENDA",
    width=250,
    height=45,
    fg_color="#C62828",
    hover_color="#8E0000",
    font=("Arial", 15, "bold"),
    command=abrir_venda
)
botao_venda.pack(pady=10)


app.mainloop()
