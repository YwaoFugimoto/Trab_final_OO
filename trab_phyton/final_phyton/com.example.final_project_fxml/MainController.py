import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from hostelapp.model import Address, Hostel
import pickle  

class ControladorPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Projeto Final")

        self.hostel_name = tk.StringVar()
        self.desc_label_text = tk.StringVar()
        self.end_label_text = tk.StringVar()
        self.date_label_text = tk.StringVar()

        self.hostel = self.read_hostel_from_file()

        self.create_widgets()

    def create_widgets(self):

        tk.Label(self.root, text="Nome do Albergue:").grid(row=0, column=0)
        tk.Label(self.root, textvariable=self.hostel_name).grid(row=0, column=1)

        tk.Label(self.root, text="Descrição:").grid(row=1, column=0)
        desc_label = tk.Label(self.root, textvariable=self.desc_label_text, wraplength=300)
        desc_label.grid(row=1, column=1)

        tk.Label(self.root, text="Endereço:").grid(row=2, column=0)
        tk.Label(self.root, textvariable=self.end_label_text).grid(row=2, column=1)

        tk.Label(self.root, text="Data de Inauguração:").grid(row=3, column=0)
        tk.Label(self.root, textvariable=self.date_label_text).grid(row=3, column=1)


        tk.Button(self.root, text="Cadastro de Hóspede", command=self.open_guest_creation).grid(row=4, column=0)
        tk.Button(self.root, text="Lista de Hóspedes", command=self.open_guest_list).grid(row=4, column=1)
        tk.Button(self.root, text="Informações do Hostel", command=self.open_hostel_info).grid(row=5, column=0)
        tk.Button(self.root, text="Cadastro de Quarto", command=self.open_room_creation).grid(row=5, column=1)

        self.atualizar_info()

    def atualizar_info(self):
        if self.hostel is not None:
            self.hostel_name.set(self.hostel.getName())
            self.desc_label_text.set(self.hostel.getDescription())
            endereco = self.hostel.getAddress()
            end_str = f"Endereco: {endereco.getAddress()}\nZip-Code: {endereco.getZipCode()}\nCidade: {endereco.getCity()}\nEstado: {endereco.getState()}\nPais: {endereco.getCountry()}"
            self.end_label_text.set(end_str)
            data = self.hostel.getInaugurationDate().toString()
            self.date_label_text.set("Desde: " + data)


    def read_hostel_from_file(self):
        try:
            with open("hostel_info.dat", "rb") as file:
                return pickle.load(file)
        except (IOError, pickle.UnpicklingError) as e:
            print("Erro ao ler as informações do albergue do arquivo:", e)
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ControladorPrincipal(root)
    root.mainloop()
