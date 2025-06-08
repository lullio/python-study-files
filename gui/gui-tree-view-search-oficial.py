import tkinter as tk
from tkinter import ttk

class TreeViewDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TreeView Demo")
        self.root.geometry("600x400")

        # Frame principal
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Treeview
        self.treeview = ttk.Treeview(self.main_frame, columns=("Conta", "Propriedades", "Fluxo de Dados"), show="tree")
        self.treeview.pack(fill=tk.BOTH, expand=True, padx=10, pady=(10, 5))

        self.treeview.heading("#0", text="Conta")
        self.treeview.column("#0", width=200)
        self.treeview.heading("Conta", text="Conta")
        self.treeview.heading("Propriedades", text="Propriedades")
        self.treeview.heading("Fluxo de Dados", text="Fluxo de Dados")
        self.treeview.column("Propriedades", width=150)
        self.treeview.column("Fluxo de Dados", width=150)

        self.insert_items()

        # Campo de busca
        self.search_frame = tk.Frame(self.main_frame)
        self.search_frame.pack(fill=tk.X, padx=10, pady=5)

        self.search_label = tk.Label(self.search_frame, text="Buscar:")
        self.search_label.pack(side=tk.LEFT)

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.search_entry.bind("<KeyRelease>", self.search)

        # Armazenar todos os itens com seus pais
        self.original_items = self.get_all_items_with_parents()

    def insert_items(self):
        root_node = self.treeview.insert("", tk.END, text="Documentos", values=("Documentos", "Root", "N/A"), open=True)
        pictures_node = self.treeview.insert("", tk.END, text="Imagens", values=("Imagens", "Root", "N/A"), open=True)

        doc1 = self.treeview.insert(root_node, tk.END, text="Trabalho.docx", values=("Documento", "Fluxo 1", "N/A"))
        doc2 = self.treeview.insert(root_node, tk.END, text="Notas.txt", values=("Texto", "Fluxo 2", "N/A"))
        self.treeview.insert(doc1, tk.END, text="Versão 1", values=("Versão", "Fluxo 1.1", "N/A"))
        self.treeview.insert(doc2, tk.END, text="Notas Adicionais", values=("Notas", "Fluxo 2.1", "N/A"))

        pic1 = self.treeview.insert(pictures_node, tk.END, text="Foto1.jpg", values=("Imagem", "Fluxo 3", "N/A"))
        pic2 = self.treeview.insert(pictures_node, tk.END, text="Foto2.png", values=("Imagem", "Fluxo 4", "N/A"))
        self.treeview.insert(pic1, tk.END, text="Foto1 Versão 1", values=("Versão", "Fluxo 3.1", "N/A"))
        self.treeview.insert(pic2, tk.END, text="Foto2 Versão 2", values=("Versão", "Fluxo 4.1", "N/A"))

    def get_all_items_with_parents(self):
        items_with_parents = []

        def recurse(parent):
            for child in self.treeview.get_children(parent):
                items_with_parents.append((child, parent))
                recurse(child)

        recurse("")
        return items_with_parents

    def hide_all_items(self):
        for item_id, _ in self.original_items:
            self.treeview.detach(item_id)

    def show_path_to_item(self, item):
        """Reatacha o item, seus pais e filhos"""
        # Reatachar pais
        current = item
        while current:
            parent = self.treeview.parent(current)
            self.treeview.reattach(current, parent, tk.END)
            self.treeview.item(parent, open=True)
            current = parent

        # Reatachar filhos (caso tenha)
        def show_children(i):
            for child in self.treeview.get_children(i):
                self.treeview.reattach(child, i, tk.END)
                show_children(child)

        show_children(item)

    def search(self, event):
        search_term = self.search_entry.get().lower()
        self.hide_all_items()

        if not search_term:
            for item_id, parent_id in self.original_items:
                self.treeview.reattach(item_id, parent_id, tk.END)
                self.treeview.item(item_id, open=False)

            # Expandir níveis principais
            for item in self.treeview.get_children():
                self.treeview.item(item, open=True)
            return

        # Se tiver termo, aplicar filtro
        for item_id, _ in self.original_items:
            if self.matches_search(item_id, search_term):
                self.show_path_to_item(item_id)

    def matches_search(self, item, term):
        """Verifica se o item bate com o termo de busca"""
        text = self.treeview.item(item, "text").lower()
        values = [str(val).lower() for val in self.treeview.item(item, "values")]
        return term in text or any(term in val for val in values)

if __name__ == "__main__":
    root = tk.Tk()
    app = TreeViewDemoApp(root)
    root.mainloop()
