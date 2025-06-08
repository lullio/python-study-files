import tkinter as tk
from tkinter import ttk

class TreeViewDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TreeView Demo")
        self.root.geometry("600x400")

        # Criar um frame para o Treeview e o campo de busca
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Criar o Treeview
        self.treeview = ttk.Treeview(self.main_frame, columns=("Conta", "Propriedades", "Fluxo de Dados"), show="tree")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))

        # Definir a coluna principal (a primeira coluna)
        self.treeview.heading("#0", text="Conta")

        # Definir as colunas adicionais
        self.treeview.column("#0", width=200)  # Largura da coluna principal
        self.treeview.heading("Conta", text="Conta")
        self.treeview.heading("Propriedades", text="Propriedades")
        self.treeview.heading("Fluxo de Dados", text="Fluxo de Dados")
        self.treeview.column("Propriedades", width=150)
        self.treeview.column("Fluxo de Dados", width=150)

        # Inserir itens no Treeview
        self.insert_items()

        # Campo de busca
        self.search_frame = tk.Frame(self.main_frame)
        self.search_frame.pack(fill=tk.X, padx=10, pady=5)

        self.search_label = tk.Label(self.search_frame, text="Buscar:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.search_entry.bind("<KeyRelease>", self.search)

        # Armazenar todos os itens para restaurar depois
        self.all_items = self.get_all_items()

    def insert_items(self):
        """ Inserir itens na estrutura da árvore """
        # Adicionar nós principais
        root_node = self.treeview.insert("", tk.END, text="Documentos", values=("Documentos", "Root", "N/A"), open=True)
        pictures_node = self.treeview.insert("", tk.END, text="Imagens", values=("Imagens", "Root", "N/A"), open=True)
        
        # Adicionar sub-nós
        doc1 = self.treeview.insert(root_node, tk.END, text="Trabalho.docx", values=("Documento", "Fluxo 1", "N/A"))
        doc2 = self.treeview.insert(root_node, tk.END, text="Notas.txt", values=("Texto", "Fluxo 2", "N/A"))
        
        self.treeview.insert(doc1, tk.END, text="Versão 1", values=("Versão", "Fluxo 1.1", "N/A"))
        self.treeview.insert(doc2, tk.END, text="Notas Adicionais", values=("Notas", "Fluxo 2.1", "N/A"))

        pic1 = self.treeview.insert(pictures_node, tk.END, text="Foto1.jpg", values=("Imagem", "Fluxo 3", "N/A"))
        pic2 = self.treeview.insert(pictures_node, tk.END, text="Foto2.png", values=("Imagem", "Fluxo 4", "N/A"))

        self.treeview.insert(pic1, tk.END, text="Foto1 Versão 1", values=("Versão", "Fluxo 3.1", "N/A"))
        self.treeview.insert(pic2, tk.END, text="Foto2 Versão 2", values=("Versão", "Fluxo 4.1", "N/A"))

    def get_all_items(self):
        """ Retornar todos os itens da Treeview em uma lista """
        all_items = []
        for item in self.treeview.get_children():
            all_items.append(item)
            all_items.extend(self.get_children(item))
        return all_items

    def get_children(self, parent):
        """ Retornar todos os filhos de um item """
        children = []
        for child in self.treeview.get_children(parent):
            children.append(child)
            children.extend(self.get_children(child))
        return children

    def search(self, event):
        """ Filtrar itens no Treeview com base na entrada de busca """
        search_term = self.search_entry.get().lower()

        # Ocultar todos os itens inicialmente
        self.hide_all_items()

        # Mostrar apenas os itens que correspondem à busca
        self.apply_filter(search_term)

    def hide_all_items(self):
        """ Ocultar todos os itens da Treeview """
        for item in self.all_items:
            self.treeview.item(item, open=False)
            self.treeview.detach(item)

    def apply_filter(self, search_term):
        """ Aplicar filtro aos itens e exibir apenas os que correspondem à busca """
        for item in self.all_items:
            if self.search_recursive(item, search_term):
                self.treeview.reattach(item, "", tk.END)

    def search_recursive(self, item, search_term):
        """ Buscar recursivamente por todos os itens e sub-itens """
        # Verifica se o texto da busca está no texto da coluna principal (#0) ou nos valores das colunas
        item_text = self.treeview.item(item, "text").lower()
        item_values = self.treeview.item(item, "values")
        if (search_term in item_text) or any(search_term in str(value).lower() for value in item_values):
            self.treeview.item(item, open=True)
            return True
        
        # Verificar todos os filhos do item
        found = False
        for child in self.treeview.get_children(item):
            if self.search_recursive(child, search_term):
                found = True
        
        return found

if __name__ == "__main__":
    root = tk.Tk()
    app = TreeViewDemoApp(root)
    root.mainloop()