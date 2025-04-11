import tkinter as tk
from tkinter import ttk

# Cores e estilo
COR_BG = "#f5f5f5"
COR_PRIMARY = "#4a90e2"
COR_FONTE = "#333333"
FONTE_PADRAO = ("Segoe UI", 10)

# janela principal
janela = tk.Tk()
janela.title("Interface")
janela.configure(bg=COR_BG)
janela.geometry("400x300")
janela.resizable(False, False)

# centralizar na tela
janela.update_idletasks()
largura = janela.winfo_width()
altura = janela.winfo_height()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela // 2) - (largura // 2)
y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{x}+{y}")

# estilo com ttk
style = ttk.Style(janela)
style.theme_use("default")

style.configure("TButton",
    font=FONTE_PADRAO,
    foreground="white",
    background=COR_PRIMARY,
    padding=10)
style.map("TButton", background=[("active", "#357ABD")])

style.configure("TLabel",
    background=COR_BG,
    foreground=COR_FONTE,
    font=FONTE_PADRAO)

# Estilo para o Frame
# Estilo para Entry
style.configure("TEntry",
    font=FONTE_PADRAO,
    foreground=COR_FONTE,
    padding=5)

# elementos da interface
label = ttk.Label(janela, text="Bem-vindo ao app!")
label.pack(pady=20)

# adicionando a caixa de texto
caixa_texto = ttk.Entry(janela, width=30)
caixa_texto.pack(pady=10)

botao = ttk.Button(janela, text="Clique aqui")
botao.pack()

janela.mainloop()
