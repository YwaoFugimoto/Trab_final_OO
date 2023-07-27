import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from hostelapp.model import Guest, Address, Title
from datetime import date

class GuestCreationController:
    def __init__(self, root):
        self.root = root
        self.root.title("Criação de Hóspede")

        self.nome_hospede = tk.StringVar()
        self.sobrenome_hospede = tk.StringVar()
        self.endereco_hospede = tk.StringVar()
        self.email_hospede = tk.StringVar()
        self.cidade_hospede = tk.StringVar()
        self.estado_hospede = tk.StringVar()
        self.cep_hospede = tk.StringVar()
        self.pais_hospede = tk.StringVar()
        self.data_nascimento_hospede = tk.StringVar()
        self.titulo_hospede = tk.StringVar()

        self.criar_widgets()

    def criar_widgets(self):
        tk.Label(self.root, text="Nome:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.nome_hospede).grid(row=0, column=1)
        
        tk.Label(self.root, text="Sobrenome:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.sobrenome_hospede).grid(row=1, column=1)
        
        tk.Label(self.root, text="Endereço:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.endereco_hospede).grid(row=2, column=1)
        
        tk.Label(self.root, text="E-mail:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.email_hospede).grid(row=3, column=1)
        
        tk.Label(self.root, text="Cidade:").grid(row=4, column=0)
        tk.Entry(self.root, textvariable=self.cidade_hospede).grid(row=4, column=1)
        
        tk.Label(self.root, text="Estado:").grid(row=5, column=0)
        tk.Entry(self.root, textvariable=self.estado_hospede).grid(row=5, column=1)
        
        tk.Label(self.root, text="CEP:").grid(row=6, column=0)
        tk.Entry(self.root, textvariable=self.cep_hospede).grid(row=6, column=1)
        
        tk.Label(self.root, text="País:").grid(row=7, column=0)
        tk.Entry(self.root, textvariable=self.pais_hospede).grid(row=7, column=1)
        
        tk.Label(self.root, text="Data de Nascimento:").grid(row=8, column=0)
        tk.Entry(self.root, textvariable=self.data_nascimento_hospede).grid(row=8, column=1)

        tk.Label(self.root, text="Título:").grid(row=9, column=0)
        opcoes_titulo = ["Sr.", "Sra.", "Srta.", "Dr."] 
        self.titulo_hospede.set(opcoes_titulo[0])
        ttk.Combobox(self.root, textvariable=self.titulo_hospede, values=opcoes_titulo).grid(row=9, column=1)

        tk.Button(self.root, text="Enviar", command=self.cadastrar_hospede).grid(row=10, column=0, columnspan=2)

    def cadastrar_hospede(self):
        hospede = Guest()
        hospede.setName(self.nome_hospede.get())
        hospede.setLastName(self.sobrenome_hospede.get())
        endereco_hospede = Address()
        endereco_hospede.setCity(self.cidade_hospede.get())
        endereco_hospede.setCountry(self.pais_hospede.get())
        endereco_hospede.setState(self.estado_hospede.get())
        endereco_hospede.setZipCode(self.cep_hospede.get())
        endereco_hospede.setAddress(self.endereco_hospede.get())
        hospede.setAddress(endereco_hospede)
        hospede.setEmail(self.email_hospede.get())
        data = date.today()

        ano, mes, dia = map(int, self.data_nascimento_hospede.get().split('-'))
        data = date(ano, mes, dia)
        hospede.setBirthDate(data)
        titulo_str = self.titulo_hospede.get()
        titulo = Title[titulo_str]
        hospede.setTitle(titulo)

        mensagem = "Hóspede cadastrado com sucesso!" 
        messagebox.showinfo("Sucesso", mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = GuestCreationController(root)
    root.mainloop()
