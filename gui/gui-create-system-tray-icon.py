import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import os

class ChatGPTManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Conversas com ChatGPT")
        self.create_menu()
        self.create_widgets()

        # Ajusta o tamanho da GUI para se adaptar ao conteúdo
        self.root.update_idletasks()
        self.root.geometry(f"{self.root.winfo_width()}x{self.root.winfo_height()}")

        self.prompts = {
            "UX": ["Análise de usabilidade", "Wireframes", "Fluxo de usuário"],
            "Analytics": ["Relatório de vendas", "Análise de KPIs", "Previsão de vendas"],
            "Programação": ["Refatoração de código", "Documentação de API", "Testes unitários"],
            "Gerar Conteúdo": ["Artigo de blog", "Postagem em redes sociais", "E-mail marketing"],
            "Tirar Dúvidas": ["Dúvida sobre código", "Pergunta de matemática", "Questão de física"],
            "Resumir Textos": ["Resumo de artigo científico", "Resumo de livro", "Resumo de notícia"],
            "Anexos": ["Anexo para revisão", "Anexo de projeto", "Anexo de pesquisa"]
        }

    def create_menu(self):
        # Criação do menu
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menu "Arquivo"
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Abrir", command=self.open_file)
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.root.quit)

        # Menu "Editar"
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Editar", menu=edit_menu)
        edit_menu.add_command(label="Desfazer", command=self.show_info)
        edit_menu.add_command(label="Refazer", command=self.show_info)
        edit_menu.add_separator()
        edit_menu.add_command(label="Copiar", command=self.show_info)
        edit_menu.add_command(label="Colar", command=self.show_info)

        # Menu "Ajuda"
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ajuda", menu=help_menu)
        help_menu.add_command(label="Sobre", command=self.show_about)

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Frame para inputs do usuário
        input_frame = tk.Frame(main_frame)
        input_frame.pack(side=tk.LEFT, padx=5, pady=10, fill=tk.Y)

        # Combobox para selecionar categoria
        self.category_label = tk.Label(input_frame, text="Categoria:")
        self.category_label.grid(row=0, column=0, sticky="w", pady=5)

        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(input_frame, textvariable=self.category_var)
        self.category_combobox['values'] = ["Selecione...", "UX", "Analytics", "Programação", "Gerar Conteúdo", "Tirar Dúvidas", "Resumir Textos", "Anexos"]
        self.category_combobox.grid(row=0, column=1, pady=5)
        self.category_combobox.current(0)
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_prompts)

        # Combobox para selecionar prompt
        self.prompt_label = tk.Label(input_frame, text="Prompt Padrão:")
        self.prompt_label.grid(row=1, column=0, sticky="w", pady=5)

        self.prompt_var = tk.StringVar()
        self.prompt_combobox = ttk.Combobox(input_frame, textvariable=self.prompt_var)
        self.prompt_combobox.grid(row=1, column=1, pady=5)

        # Campo de texto para entrada do usuário
        self.text_label = tk.Label(input_frame, text="Insira seu texto:")
        self.text_label.grid(row=2, column=0, sticky="w", pady=5)

        self.text_area = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=30, height=5)
        self.text_area.grid(row=3, column=0, columnspan=2, padx=5)

        # Checkbox para manter histórico
        self.keep_history_var = tk.BooleanVar()
        self.keep_history_checkbox = tk.Checkbutton(input_frame, text="Manter histórico de conversas", variable=self.keep_history_var)
        self.keep_history_checkbox.grid(row=4, column=0, columnspan=2, sticky="w", pady=5)

        # Checkbox para salvar no Notion
        self.save_notion_var = tk.BooleanVar()
        self.save_notion_checkbox = tk.Checkbutton(input_frame, text="Salvar dados no Notion", variable=self.save_notion_var)
        self.save_notion_checkbox.grid(row=5, column=0, columnspan=2, sticky="w", pady=5)

        # Botões organizados em uma linha
        self.button_frame = tk.Frame(input_frame)
        self.button_frame.grid(row=6, column=0, columnspan=2, pady=5)

        self.attachment_button = tk.Button(self.button_frame, text="Adicionar Anexo", command=self.add_attachment)
        self.attachment_button.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(self.button_frame, text="Enviar Solicitação", command=self.send_request)
        self.send_button.pack(side=tk.LEFT, padx=5)

        # Label para mostrar o nome do anexo
        self.attachment_path_label = tk.Label(input_frame, text="", fg="blue", wraplength=200)
        self.attachment_path_label.grid(row=7, column=0, columnspan=2, pady=5)

        # Frame para a área de resposta
        response_frame = tk.Frame(main_frame)
        response_frame.pack(side=tk.LEFT, padx=5, pady=10, fill=tk.BOTH, expand=True)

        self.response_label = tk.Label(response_frame, text="Resposta do ChatGPT:")
        self.response_label.pack(anchor="w", pady=5)

        self.response_area = scrolledtext.ScrolledText(response_frame, wrap=tk.WORD, width=30, height=4)
        self.response_area.pack(fill=tk.BOTH, expand=True)
        self.response_area.config(state=tk.DISABLED)

        # Frame para botões de resposta
        response_button_frame = tk.Frame(response_frame)
        response_button_frame.pack(anchor="w", pady=5)

        self.open_notion_button = tk.Button(response_button_frame, text="Abrir no Notion", command=self.open_notion)
        self.open_notion_button.pack(side=tk.LEFT, padx=5)

        self.open_button = tk.Button(response_button_frame, text="Abrir", command=self.open_response)
        self.open_button.pack(side=tk.LEFT, padx=5)

    def update_prompts(self, event):
        # Atualiza os prompts com base na categoria selecionada
        selected_category = self.category_var.get()
        if selected_category in self.prompts:
            self.prompt_combobox['values'] = self.prompts[selected_category]
            self.prompt_combobox.current(0)
        else:
            self.prompt_combobox.set('')
            self.prompt_combobox['values'] = []

    def add_attachment(self):
        # Função para adicionar anexo
        self.attachment_path = filedialog.askopenfilename(title="Selecione um arquivo")
        if self.attachment_path:
            filename = os.path.basename(self.attachment_path)
            self.attachment_path_label.config(text=f"Anexo: {filename}")
            self.category_combobox.set("Anexos")
            self.update_prompts(None)
        else:
            messagebox.showwarning("Nenhum Anexo", "Nenhum anexo foi selecionado.")

    def send_request(self):
        # Função para enviar a solicitação
        user_text = self.text_area.get("1.0", tk.END).strip()
        keep_history = self.keep_history_var.get()
        save_notion = self.save_notion_var.get()
        selected_category = self.category_combobox.get()
        selected_prompt = self.prompt_combobox.get()
        if user_text:
            # Aqui você pode adicionar a lógica para enviar a solicitação ao ChatGPT
            print(f"Categoria Selecionada: {selected_category}")
            print(f"Prompt Selecionado: {selected_prompt}")
            print(f"Texto do Usuário: {user_text}")
            print(f"Manter Histórico: {'Sim' if keep_history else 'Não'}")
            print(f"Salvar no Notion: {'Sim' if save_notion else 'Não'}")
            if hasattr(self, 'attachment_path'):
                print(f"Anexo: {self.attachment_path}")
            self.display_response("Aqui estará a resposta do ChatGPT.")
            messagebox.showinfo("Solicitação Enviada", "Sua solicitação foi enviada com sucesso!")
        else:
            messagebox.showwarning("Texto Vazio", "Por favor, insira um texto para enviar a solicitação.")

    def display_response(self, response_text):
        # Função para exibir a resposta do ChatGPT
        self.response_area.config(state=tk.NORMAL)
        self.response_area.delete("1.0", tk.END)
        self.response_area.insert(tk.END, response_text)
        self.response_area.config(state=tk.DISABLED)

    def open_notion(self):
        # Função para abrir a resposta no Notion
        messagebox.showinfo("Abrir no Notion", "A função de abrir no Notion ainda não está implementada.")

    def open_response(self):
        # Função para abrir a resposta diretamente
        messagebox.showinfo("Abrir Resposta", "A função de abrir a resposta diretamente ainda não está implementada.")

    def open_file(self):
        # Função para abrir um arquivo
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Abrir Arquivo", f"Arquivo selecionado: {file_path}")

    def show_about(self):
        # Função para mostrar informações sobre o aplicativo
        messagebox.showinfo("Sobre", "Gerenciador de Conversas com ChatGPT - Versão 1.0")

    def show_info(self):
        # Função para mostrar informações genéricas
        messagebox.showinfo("Informação", "Esta é uma informação genérica.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGPTManager(root)
    root.mainloop()
