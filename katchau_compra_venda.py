import customtkinter as ctk

ctk.set_appearance_mode("dark")

VERMELHO = "#C62828"
BRANCO = "#FFFFFF"
CINZA = "#1E1E1E"

app = ctk.CTk()
app.title("Katchau - Compra e Venda")
app.geometry("1000x620")
app.configure(fg_color="#111111")


def abrir_operacao(tipo):
    janela = ctk.CTkToplevel(app)
    janela.title(tipo)
    janela.geometry("470x610")
    janela.resizable(False, False)
    janela.grab_set()

    ctk.CTkLabel(
        janela, text=f"REGISTRAR {tipo.upper()}",
        font=("Arial", 22, "bold"), text_color=VERMELHO
    ).pack(pady=(25, 15))

    campos = [
        "Nome do cliente",
        "Modelo do veículo",
        "Placa",
        "Valor (R$)",
        "Cupom de desconto",
    ]

    entradas = {}
    for campo in campos:
        ctk.CTkLabel(janela, text=campo, anchor="w").pack(
            padx=55, fill="x", pady=(7, 2)
        )
        entrada = ctk.CTkEntry(
            janela, height=38, placeholder_text=f"Digite {campo.lower()}"
        )
        entrada.pack(padx=55, fill="x")
        entradas[campo] = entrada

    def registrar():
        cliente = entradas["Nome do cliente"].get().strip()
        veiculo = entradas["Modelo do veículo"].get().strip()
        placa = entradas["Placa"].get().strip()

        if not cliente or not veiculo or not placa:
            aviso.configure(
                text="Preencha cliente, veículo e placa.",
                text_color="#FF5555"
            )
            return

        aviso.configure(
            text=f"{tipo} registrada com sucesso!",
            text_color="#55CC77"
        )

    ctk.CTkButton(
        janela, text=f"REGISTRAR {tipo.upper()}",
        fg_color=VERMELHO, hover_color="#A91F1F",
        height=45, font=("Arial", 14, "bold"),
        command=registrar
    ).pack(padx=55, fill="x", pady=(25, 10))

    aviso = ctk.CTkLabel(janela, text="", font=("Arial", 13))
    aviso.pack(pady=5)


# Menu lateral
menu = ctk.CTkFrame(app, width=220, fg_color="#191919", corner_radius=0)
menu.pack(side="left", fill="y")
menu.pack_propagate(False)

ctk.CTkLabel(
    menu, text="KATCHAU", font=("Arial", 28, "bold"),
    text_color=VERMELHO
).pack(pady=(35, 45))

for item in ["Início", "Clientes", "Vendedores", "Veículos",
             "Aluguel", "Compra e Venda", "Comissões", "Histórico"]:
    ctk.CTkButton(
        menu, text=item, anchor="w",
        fg_color="transparent", hover_color="#333333",
        text_color=BRANCO, height=42
    ).pack(fill="x", padx=15, pady=3)

# Área principal
conteudo = ctk.CTkFrame(app, fg_color="#111111")
conteudo.pack(side="right", expand=True, fill="both", padx=35, pady=35)

ctk.CTkLabel(
    conteudo, text="COMPRA E VENDA DE VEÍCULOS",
    font=("Arial", 27, "bold"), text_color=BRANCO
).pack(anchor="w", pady=(35, 10))

ctk.CTkLabel(
    conteudo, text="Selecione a operação que deseja realizar.",
    font=("Arial", 15), text_color="#AAAAAA"
).pack(anchor="w", pady=(0, 40))

cards = ctk.CTkFrame(conteudo, fg_color="transparent")
cards.pack(fill="x", expand=True)

for titulo, descricao, tipo in [
    ("COMPRAR VEÍCULO", "Registrar a compra de um automóvel.",
     "Compra"),
    ("VENDER VEÍCULO", "Registrar a venda de um automóvel.",
     "Venda")
]:
    card = ctk.CTkFrame(
        cards, fg_color=CINZA, corner_radius=15, border_width=1,
        border_color="#333333"
    )
    card.pack(side="left", expand=True, fill="both", padx=12, pady=10)

    ctk.CTkLabel(
        card, text="🚗", font=("Arial", 42)
    ).pack(pady=(45, 15))

    ctk.CTkLabel(
        card, text=titulo, font=("Arial", 19, "bold"),
        text_color=VERMELHO
    ).pack(pady=10)

    ctk.CTkLabel(
        card, text=descricao, font=("Arial", 13),
        text_color="#BBBBBB", wraplength=220
    ).pack(pady=10)

    ctk.CTkButton(
        card, text="ACESSAR", height=42,
        fg_color=VERMELHO, hover_color="#A91F1F",
        command=lambda t=tipo: abrir_operacao(t)
    ).pack(padx=25, fill="x", pady=(20, 45))

app.mainloop()
