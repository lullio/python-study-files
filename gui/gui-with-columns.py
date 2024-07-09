import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Exemplo de Alinhamento")

# Frame para organizar os widgets
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Primeira linha: Label à esquerda e Combobox à direita
col4_filter_label = tk.Label(frame, text="Filtrar por Categoria:")
col4_filter_label.grid(row=0, column=0, padx=(0, 10), sticky="w", pady=10)  # Alinha à esquerda com padding à direita

col4_values = ["Categoria 1", "Categoria 2", "Categoria 3"]
col4_filter_var = tk.StringVar()
col4_filter_dropdown = ttk.Combobox(frame, textvariable=col4_filter_var, values=["Todos"] + col4_values, state="readonly")
col4_filter_dropdown.grid(row=0, column=1, sticky="w")  # Alinha à esquerda

# Segunda linha: Label ao lado do Label anterior e Entry abaixo do Label
search_label = tk.Label(frame, text="Pesquisar:")
search_label.grid(row=1, column=0, padx=(20, 10), sticky="w")  # Alinha à esquerda com padding à direita

search_entry = ttk.Entry(frame)
search_entry.grid(row=1, column=1, sticky="we", padx=(0, 10))  # Preenche horizontalmente e alinha à esquerda

root.mainloop()
