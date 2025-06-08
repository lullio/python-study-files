import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser, simpledialog

class TkinterDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Demo App")
        self.root.geometry("800x600")  # Define a largura e altura inicial da janela

        # Configura a janela principal com uma barra de rolagem
        self.create_widgets()

    def create_widgets(self):
        # Frame principal para a rolagem
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas para a rolagem
        self.canvas = tk.Canvas(main_frame)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Barra de rolagem
        self.scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")

        # Frame para o conteúdo da rolagem
        self.scrollable_frame = tk.Frame(self.canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        # Adiciona o frame de rolagem ao canvas
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Configura o menu
        self.create_menu()

        # Notebook (abas) para organizar os widgets
        self.notebook = ttk.Notebook(self.scrollable_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Cria abas para diferentes categorias de widgets
        self.create_widgets_tabs()

    def create_widgets_tabs(self):
        # Aba 1: Entrada de Dados
        self.tab1 = tk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Entrada de Dados")

        # Label
        self.label = tk.Label(self.tab1, text="Olá, Tkinter!", font=("Arial", 16))
        self.label.pack(pady=10)

        # Entry
        self.entry_label = tk.Label(self.tab1, text="Digite algo:")
        self.entry_label.pack(pady=5)

        self.entry = tk.Entry(self.tab1, width=30)
        self.entry.pack(pady=5)

        # Button
        self.show_message_button = tk.Button(self.tab1, text="Mostrar Mensagem", command=self.show_message)
        self.show_message_button.pack(pady=5)

        # Checkbutton
        self.check_var = tk.BooleanVar()
        self.checkbutton = tk.Checkbutton(self.tab1, text="Marcar isso", variable=self.check_var)
        self.checkbutton.pack(pady=5)

        # Radiobutton
        self.radio_var = tk.StringVar(value="Opção 1")
        self.radio1 = tk.Radiobutton(self.tab1, text="Opção 1", variable=self.radio_var, value="Opção 1")
        self.radio2 = tk.Radiobutton(self.tab1, text="Opção 2", variable=self.radio_var, value="Opção 2")
        self.radio1.pack(pady=5)
        self.radio2.pack(pady=5)

        # Combobox
        self.combobox_label = tk.Label(self.tab1, text="Escolha uma opção:")
        self.combobox_label.pack(pady=5)

        self.combobox = ttk.Combobox(self.tab1, values=["Item 1", "Item 2", "Item 3"])
        self.combobox.pack(pady=5)

        # Spinbox
        self.spinbox_label = tk.Label(self.tab1, text="Escolha um número:")
        self.spinbox_label.pack(pady=5)

        self.spinbox = tk.Spinbox(self.tab1, from_=1, to=10)
        self.spinbox.pack(pady=5)

        # Scale
        self.scale_label = tk.Label(self.tab1, text="Ajuste o valor:")
        self.scale_label.pack(pady=5)

        self.scale = tk.Scale(self.tab1, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scale.pack(pady=5)

        # Listbox
        self.listbox_label = tk.Label(self.tab1, text="Itens disponíveis:")
        self.listbox_label.pack(pady=5)

        self.listbox = tk.Listbox(self.tab1, height=4)
        self.listbox.pack(pady=5)
        for item in ["Item A", "Item B", "Item C"]:
            self.listbox.insert(tk.END, item)

        # Aba 2: Texto e Cor
        self.tab2 = tk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Texto e Cor")

        # Text
        self.text_label = tk.Label(self.tab2, text="Texto:")
        self.text_label.pack(pady=5)

        self.text_area = tk.Text(self.tab2, height=5, width=40)
        self.text_area.pack(pady=5)

        # Color Chooser Button
        self.color_button = tk.Button(self.tab2, text="Escolher Cor", command=self.choose_color)
        self.color_button.pack(pady=5)

        # Aba 3: Arquivo e Diálogo
        self.tab3 = tk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Arquivo e Diálogo")

        # File Dialog Button
        self.file_button = tk.Button(self.tab3, text="Abrir Arquivo", command=self.open_file)
        self.file_button.pack(pady=5)

        # Dialogs
        self.dialog_button = tk.Button(self.tab3, text="Abrir Diálogo", command=self.show_dialog)
        self.dialog_button.pack(pady=5)

        # Aba 4: Menu e Treeview
        self.tab4 = tk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Menu e Treeview")

        # Menu List (Listbox com cabeçalho)
        self.menu_label = tk.Label(self.tab4, text="Menu List")
        self.menu_label.pack(pady=5)

        self.menu_list = tk.Listbox(self.tab4, height=6)
        self.menu_list.pack(pady=5)
        for item in ["Menu Item 1", "Menu Item 2", "Menu Item 3"]:
            self.menu_list.insert(tk.END, item)

        # Treeview
        self.treeview_label = tk.Label(self.tab4, text="Treeview")
        self.treeview_label.pack(pady=5)

        self.treeview = ttk.Treeview(self.tab4, columns=("col1", "col2"), show='headings')
        self.treeview.heading("col1", text="Coluna 1")
        self.treeview.heading("col2", text="Coluna 2")
        self.treeview.pack(pady=5)

        # Adiciona algumas linhas de exemplo
        for i in range(5):
            self.treeview.insert("", tk.END, values=(f"Item {i+1}", f"Valor {i+1}"))

    def create_menu(self):
        """ Cria o menu da aplicação """
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)

        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Desfazer", command=self.show_info)
        edit_menu.add_command(label="Refazer", command=self.show_info)

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=help_menu)
        help_menu.add_command(label="Sobre", command=self.show_about)

    def show_message(self):
        """ Exibe uma mensagem com o texto da Entry """
        user_text = self.entry.get()
        messagebox.showinfo("Mensagem", f"Você digitou: {user_text}")

    def choose_color(self):
        """ Abre o seletor de cor e exibe a cor escolhida """
        color = colorchooser.askcolor()[1]
        if color:
            self.root.config(bg=color)

    def open_file(self):
        """ Abre o diálogo de seleção de arquivo """
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Arquivo Selecionado", f"Arquivo selecionado: {file_path}")

    def show_dialog(self):
        """ Abre um diálogo para entrada de texto """
        user_input = simpledialog.askstring("Entrada", "Digite algo:")
        if user_input:
            messagebox.showinfo("Entrada", f"Você digitou: {user_input}")

    def show_about(self):
        """ Exibe informações sobre a aplicação """
        messagebox.showinfo("Sobre", "Tkinter Demo App - Versão 1.0")

    def show_info(self):
        """ Exibe uma mensagem de informação genérica """
        messagebox.showinfo("Informação", "Você clicou em um item de menu.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TkinterDemoApp(root)
    root.mainloop()
