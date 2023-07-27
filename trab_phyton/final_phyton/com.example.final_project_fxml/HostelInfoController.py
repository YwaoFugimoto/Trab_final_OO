import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from hostelapp.model import Address, Hostel
from datetime import datetime
import pickle

class HostelInfoController:
    def __init__(self, root):
        self.root = root
        self.root.title("Informações do Albergue")

        self.hostel_name = tk.StringVar()
        self.hostel_end = tk.StringVar()
        self.hostel_tel = tk.StringVar()
        self.hostel_mail = tk.StringVar()
        self.hostel_desc = tk.StringVar()
        self.hostel_date = tk.StringVar()
        self.hostel_zip = tk.StringVar()
        self.hostel_cidade = tk.StringVar()
        self.hostel_pais = tk.StringVar()
        self.hostel_estado = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Nome do Albergue:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.hostel_name).grid(row=0, column=1)

        tk.Label(self.root, text="Endereço:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.hostel_end).grid(row=1, column=1)

        tk.Label(self.root, text="Telefone:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.hostel_tel).grid(row=2, column=1)

        tk.Label(self.root, text="E-mail:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.hostel_mail).grid(row=3, column=1)

        tk.Label(self.root, text="Descrição:").grid(row=4, column=0)
        tk.Entry(self.root, textvariable=self.hostel_desc).grid(row=4, column=1)

        tk.Label(self.root, text="Data de Inauguração:").grid(row=5, column=0)
        tk.Entry(self.root, textvariable=self.hostel_date).grid(row=5, column=1)

        tk.Label(self.root, text="CEP:").grid(row=6, column=0)
        tk.Entry(self.root, textvariable=self.hostel_zip).grid(row=6, column=1)

        tk.Label(self.root, text="Cidade:").grid(row=7, column=0)
        tk.Entry(self.root, textvariable=self.hostel_cidade).grid(row=7, column=1)

        tk.Label(self.root, text="País:").grid(row=8, column=0)
        tk.Entry(self.root, textvariable=self.hostel_pais).grid(row=8, column=1)

        tk.Label(self.root, text="Estado:").grid(row=9, column=0)
        tk.Entry(self.root, textvariable=self.hostel_estado).grid(row=9, column=1)

        tk.Button(self.root, text="Salvar", command=self.save_info).grid(row=10, column=0, columnspan=2)

    def save_info(self):
        nome = self.hostel_name.get()
        end = self.hostel_end.get()
        tel = self.hostel_tel.get()
        mail = self.hostel_mail.get()
        desc = self.hostel_desc.get()
        data_str = self.hostel_date.get()
        zip_code = self.hostel_zip.get()
        cidade = self.hostel_cidade.get()
        pais = self.hostel_pais.get()
        estado = self.hostel_estado.get()

        try:
            date_format = "%d/%m/%Y"
            date = datetime.strptime(data_str, date_format).date()

            address = Address()
            address.setZipCode(zip_code)
            address.setAddress(end)
            address.setCity(cidade)
            address.setCountry(pais)
            address.setState(estado)

            hostel = Hostel.getHostel()
            hostel.setName(nome)
            hostel.setAddress(address)
            hostel.setPhone(tel)
            hostel.setContactEmail(mail)
            hostel.setDescription(desc)
            hostel.setInaugurationDate(date)

            self.save_hostel_info(hostel)

            print("As informações do albergue foram salvas com sucesso!")
        except ValueError:
            print("Erro: Formato de data inválido. Use o formato dd/MM/yyyy.")
        except IOError as e:
            print("Erro ao salvar as informações do albergue:", e)

        message = "Informações salvas com sucesso!"
        messagebox.showinfo("Sucesso", message)

    def save_hostel_info(self, hostel):
        filename = "hostel_info.dat"
        with open(filename, "wb") as file:
            pickle.dump(hostel, file)

if __name__ == "__main__":
    root = tk.Tk()
    app = HostelInfoController(root)
    root.mainloop()
