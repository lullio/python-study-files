import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

class ChatGPTManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciador de Conversas com ChatGPT")
        self.root.geometry("700x400")
        
        self.create_widgets()
        self.prompts = {
            "UX": ["Análise de usabilidade", "Wireframes", "Fluxo de usuário"],
            "Analytics": ["Relatório de vendas", "Análise de KPIs", "Previsão de vendas"],
            "Programação": ["Refatoração de código", "Documentação de API", "Testes unitários"],
            "Gerar Conteúdo": ["Artigo de blog", "Postagem em redes sociais", "E-mail marketing"],
            "Tirar Dúvidas": ["Dúvida sobre código", "Pergunta de matemática", "Questão de física"],
            "Resumir Textos": ["Resumo de artigo científico", "Resumo de livro", "Resumo de notícia"]
        }

    def create_widgets(self):
        # Frame para organização dos widgets
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Combobox para selecionar categoria
        self.category_label = tk.Label(frame, text="Selecione uma Categoria:")
        self.category_label.grid(row=0, column=0, sticky="w", pady=5)

        self.category_var = tk.StringVar()
        self.category_combobox = ttk.Combobox(frame, textvariable=self.category_var)
        self.category_combobox['values'] = ["Selecione...", "UX", "Analytics", "Programação", "Gerar Conteúdo", "Tirar Dúvidas", "Resumir Textos"]
        self.category_combobox.grid(row=0, column=1, sticky="ew", pady=5)
        self.category_combobox.current(0)
        self.category_combobox.bind("<<ComboboxSelected>>", self.update_prompts)

        # Combobox para selecionar prompt
        self.prompt_label = tk.Label(frame, text="Selecione um Prompt Padrão:")
        self.prompt_label.grid(row=1, column=0, sticky="w", pady=5)

        self.prompt_var = tk.StringVar()
        self.prompt_combobox = ttk.Combobox(frame, textvariable=self.prompt_var)
        self.prompt_combobox.grid(row=1, column=1, sticky="ew", pady=5)

        # Campo de texto grande para entrada e saída lado a lado
        text_frame = tk.Frame(frame)
        text_frame.grid(row=2, column=0, columnspan=2, pady=5)

        self.text_label = tk.Label(text_frame, text="Insira seu texto:")
        self.text_label.grid(row=0, column=0, sticky="w", pady=5)

        self.text_area = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=30, height=10)
        self.text_area.grid(row=1, column=0, padx=5)

        self.response_label = tk.Label(text_frame, text="Resposta do ChatGPT:")
        self.response_label.grid(row=0, column=1, sticky="w", pady=5)

        self.response_area = scrolledtext.ScrolledText(text_frame, wrap=tk.WORD, width=30, height=10)
        self.response_area.grid(row=1, column=1, padx=5)
        self.response_area.config(state=tk.DISABLED)
        
        # Checkbox para manter histórico
        self.keep_history_var = tk.BooleanVar()
        self.keep_history_checkbox = tk.Checkbutton(frame, text="Manter histórico de conversas", variable=self.keep_history_var)
        self.keep_history_checkbox.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)

        # Checkbox para salvar no Notion
        self.save_notion_var = tk.BooleanVar()
        self.save_notion_checkbox = tk.Checkbutton(frame, text="Salvar dados no Notion", variable=self.save_notion_var)
        self.save_notion_checkbox.grid(row=4, column=0, columnspan=2, sticky="w", pady=5)

        # Botões organizados em uma linha
        self.button_frame = tk.Frame(frame)
        self.button_frame.grid(row=5, column=0, columnspan=2, pady=5)

        self.attachment_button = tk.Button(self.button_frame, text="Adicionar Anexo", command=self.add_attachment)
        self.attachment_button.pack(side=tk.LEFT, padx=5)

        self.send_button = tk.Button(self.button_frame, text="Enviar Solicitação", command=self.send_request)
        self.send_button.pack(side=tk.LEFT, padx=5)

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
            messagebox.showinfo("Anexo Adicionado", f"Anexo adicionado: {self.attachment_path}")
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

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGPTManager(root)
    root.mainloop()
