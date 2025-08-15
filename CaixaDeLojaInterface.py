print("=== SUPERTECH - SUA LOJA DE COMPUTADORES ===")

import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# --- Funções do aplicativo ---

def adicionar_produto():
    try:
        index = lista_produtos.curselection()[0]
        quantidade = int(entrada_quantidade.get())
        
        if quantidade <= 0:
            messagebox.showerror("Erro", "Quantidade deve ser maior que zero.")
            return
        
        nome, preco = produtos[index]
        total_item = preco * quantidade
        carrinho.append((nome, quantidade, total_item))
        atualizar_carrinho()
        entrada_quantidade.delete(0, tk.END)
        entrada_quantidade.insert(0, "1")
        
    except IndexError:
        messagebox.showerror("Erro", "Selecione um produto.")
    except ValueError:
        messagebox.showerror("Erro", "Digite uma quantidade válida.")

def remover_produto():
    try:
        selected_item = lista_carrinho.selection()[0]
        index = lista_carrinho.index(selected_item)
        del carrinho[index]
        atualizar_carrinho()
    except IndexError:
        messagebox.showerror("Erro", "Selecione um produto no carrinho para remover.")

def esvaziar_carrinho():
    if not carrinho:
        messagebox.showinfo("Carrinho vazio", "O carrinho já está vazio.")
        return
    
    resposta = messagebox.askyesno("Confirmar", "Tem certeza que deseja esvaziar o carrinho?")
    if resposta:
        carrinho.clear()
        atualizar_carrinho()
        messagebox.showinfo("Sucesso", "O carrinho foi esvaziado.")

def atualizar_carrinho():
    lista_carrinho.delete(*lista_carrinho.get_children())
    total = 0
    for nome, quantidade, total_item in carrinho:
        lista_carrinho.insert("", "end", values=(nome, quantidade, f"R$ {total_item:.2f}"))
        total += total_item
    
    desconto = 0
    if total > 300:
        desconto = total * 0.10
        total -= desconto

    label_total.config(text=f"Total: R$ {total:.2f}")
    if desconto > 0:
        label_desconto.config(text=f"Você economizou: R$ {desconto:.2f}")
    else:
        label_desconto.config(text="")

# Finalizar compra com confirmação
def finalizar_compra():
    if not carrinho:
        messagebox.showinfo("Carrinho vazio", "Adicione produtos antes de finalizar.")
        return

    resposta = messagebox.askyesno("Confirmar Compra", "Deseja realmente finalizar a compra?")
    if resposta:
        forma_pagamento = combo_pagamento.get()
        if forma_pagamento == "À vista":
            messagebox.showinfo("Compra finalizada", "Pagamento à vista selecionado.\nObrigado pela compra!")
        elif forma_pagamento == "Parcelado em 3x":
            total = sum(item[2] for item in carrinho)
            desconto = 0
            if total > 300:
                desconto = total * 0.10
                total -= desconto
            parcela = total / 3
            messagebox.showinfo("Compra finalizada", f"Pagamento parcelado em 3x de R$ {parcela:.2f}.\nObrigado pela compra!")
        else:
            messagebox.showerror("Erro", "Selecione uma forma de pagamento.")

# --- Dados do aplicativo ---

produtos = [
    ("Monitor 24 polegadas", 650.70),
    ("Teclado 75%", 210.30),
    ("Mouse 20000 DPI", 110.25),
    ("Gabinete aquário", 410.90),
    ("Mousepad 70x30", 30.15),
    ("Filtro de linha", 64.70),
    ("Processador 4.2 GHz", 1405.25)
]

carrinho = []

# --- Configuração da janela principal ---

janela = tk.Tk()
janela.title("SuperTech - Loja de Computadores")
janela.geometry("500x600")
janela.configure(bg="#282a36")

try:
    icon_image = Image.open("icone_supertech.png")
    icon_photo = ImageTk.PhotoImage(icon_image)
    janela.iconphoto(False, icon_photo)
except FileNotFoundError:
    print("Ícone 'icone_supertech.png' não encontrado. A janela será exibida sem ícone.")

# --- Estilos de widgets (ttk) ---

style = ttk.Style()
style.theme_use('default')
style.configure("TButton", font=("Arial", 10, "bold"), background="#bd93f9", foreground="#282a36", borderwidth=0, relief="flat", padding=5)
style.map("TButton", background=[("active", "#6272a4")])

# --- Widgets e Layout ---

tk.Label(janela, text="SUPERTECH - LOJA DE COMPUTADORES", font=("Arial", 16, "bold"), fg="#f8f8f2", bg="#282a36").pack(pady=10)

# Lista de produtos
frame_produtos = tk.Frame(janela, bg="#282a36")
frame_produtos.pack(pady=5)
tk.Label(frame_produtos, text="Produtos disponíveis:", font=("Arial", 10, "bold"), bg="#282a36", fg="#f8f8f2").pack()

lista_produtos = tk.Listbox(frame_produtos, width=60, height=7, font=("Arial", 10), bg="#44475a", fg="#f8f8f2", borderwidth=1, relief="solid", highlightthickness=0)
for nome, preco in produtos:
    lista_produtos.insert(tk.END, f"{nome:<40} R$ {preco:>7.2f}")
lista_produtos.pack()

# Quantidade e Adicionar
frame_qtd = tk.Frame(janela, bg="#282a36")
frame_qtd.pack(pady=5)
tk.Label(frame_qtd, text="Quantidade:", font=("Arial", 10), bg="#282a36", fg="#f8f8f2").pack(side=tk.LEFT)
entrada_quantidade = tk.Entry(frame_qtd, width=5, font=("Arial", 10), bg="#44475a", fg="#f8f8f2", borderwidth=1, relief="solid", insertbackground="#f8f8f2")
entrada_quantidade.insert(0, "1")
entrada_quantidade.pack(side=tk.LEFT, padx=5)
ttk.Button(frame_qtd, text="Adicionar ao carrinho", command=adicionar_produto).pack(side=tk.LEFT)

# Carrinho
frame_carrinho = tk.Frame(janela, bg="#282a36")
frame_carrinho.pack(pady=10)
tk.Label(frame_carrinho, text="Carrinho de compras:", font=("Arial", 10, "bold"), bg="#282a36", fg="#f8f8f2").pack()

tree_style = ttk.Style()
tree_style.configure("Treeview.Heading", font=("Arial", 10, "bold"), background="#44475a", foreground="#f8f8f2")
tree_style.configure("Treeview", font=("Arial", 10), rowheight=25, background="#44475a", foreground="#f8f8f2", fieldbackground="#44475a")

lista_carrinho = ttk.Treeview(frame_carrinho, columns=("Produto", "Qtd", "Preço"), show="headings", height=7, style="Treeview")
lista_carrinho.heading("Produto", text="Produto")
lista_carrinho.heading("Qtd", text="Qtd")
lista_carrinho.heading("Preço", text="Preço")
lista_carrinho.column("Produto", width=250)
lista_carrinho.column("Qtd", width=50, anchor="center")
lista_carrinho.column("Preço", width=100, anchor="e")
lista_carrinho.pack()

# Botões do carrinho
frame_botoes_carrinho = tk.Frame(janela, bg="#282a36")
frame_botoes_carrinho.pack(pady=5)
ttk.Button(frame_botoes_carrinho, text="Remover item", command=remover_produto).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_botoes_carrinho, text="Esvaziar carrinho", command=esvaziar_carrinho).pack(side=tk.LEFT)

# Total e pagamento
label_total = tk.Label(janela, text="Total: R$ 0.00", font=("Arial", 12, "bold"), fg="#f8f8f2", bg="#282a36")
label_total.pack(pady=(5, 0))

label_desconto = tk.Label(janela, text="", font=("Arial", 10, "bold"), bg="#282a36", fg="#bd93f9")
label_desconto.pack(pady=(0, 5))

tk.Label(janela, text="Forma de pagamento:", font=("Arial", 10), bg="#282a36", fg="#f8f8f2").pack()
combo_pagamento = ttk.Combobox(janela, values=["À vista", "Parcelado em 3x"], font=("Arial", 10))
combo_pagamento.pack(pady=5)

# Botão finalizar
ttk.Button(janela, text="Finalizar compra", command=finalizar_compra).pack(pady=10)

janela.mainloop()
