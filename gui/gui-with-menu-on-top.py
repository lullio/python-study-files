import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def new_file():
    messagebox.showinfo("Novo Arquivo", "Novo arquivo criado!")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        messagebox.showinfo("Abrir Arquivo", f"Abrindo arquivo: {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write("Arquivo salvo!")
        messagebox.showinfo("Salvar Arquivo", f"Arquivo salvo: {file_path}")

def cut():
    messagebox.showinfo("Cortar", "Cortar selecionado!")

def copy():
    messagebox.showinfo("Copiar", "Copiar selecionado!")

def paste():
    messagebox.showinfo("Colar", "Colar selecionado!")

def about():
    messagebox.showinfo("Sobre", "Este é um exemplo de menu usando Tkinter.")

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Menu Tkinter")
root.geometry("400x300")

# Criação da barra de menu
menu_bar = tk.Menu(root)

# Menu Arquivo
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Novo", command=new_file)
file_menu.add_command(label="Abrir...", command=open_file)
file_menu.add_command(label="Salvar", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Sair", command=root.quit)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)

# Menu Editar
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cortar", command=cut)
edit_menu.add_command(label="Copiar", command=copy)
edit_menu.add_command(label="Colar", command=paste)
menu_bar.add_cascade(label="Editar", menu=edit_menu)

# Menu Ajuda
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Sobre", command=about)
menu_bar.add_cascade(label="Ajuda", menu=help_menu)

# Adicionar a barra de menu à janela principal
root.config(menu=menu_bar)

# Iniciar o loop principal da interface gráfica
root.mainloop()
