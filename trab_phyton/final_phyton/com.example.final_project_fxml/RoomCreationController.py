import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from hostelapp.model import Hostel, Room, RoomType

class RoomCreationController:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Quarto")

        self.num_room = tk.StringVar()
        self.name_room = tk.StringVar()
        self.floor_room = tk.StringVar()
        self.desc_room = tk.StringVar()
        self.dim_room = tk.StringVar()
        self.daily_room = tk.StringVar()
        self.type_room = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Número do Quarto:").grid(row=0, column=0)
        tk.Entry(self.root, textvariable=self.num_room).grid(row=0, column=1)

        tk.Label(self.root, text="Nome do Quarto:").grid(row=1, column=0)
        tk.Entry(self.root, textvariable=self.name_room).grid(row=1, column=1)

        tk.Label(self.root, text="Andar do Quarto:").grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.floor_room).grid(row=2, column=1)

        tk.Label(self.root, text="Descrição do Quarto:").grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.desc_room).grid(row=3, column=1)

        tk.Label(self.root, text="Dimensão do Quarto:").grid(row=4, column=0)
        tk.Entry(self.root, textvariable=self.dim_room).grid(row=4, column=1)

        tk.Label(self.root, text="Taxa Diária do Quarto:").grid(row=5, column=0)
        tk.Entry(self.root, textvariable=self.daily_room).grid(row=5, column=1)

        tk.Label(self.root, text="Tipo do Quarto:").grid(row=6, column=0)
        opcoes_tipo_quarto = ["Simples", "Duplo", "Triplo", "Suíte"]  # Substitua pelas opções de tipo adequadas
        self.type_room.set(opcoes_tipo_quarto[0])
        ttk.Combobox(self.root, textvariable=self.type_room, values=opcoes_tipo_quarto).grid(row=6, column=1)

        tk.Button(self.root, text="Cadastrar", command=self.cadastrar_quarto).grid(row=7, column=0, columnspan=2)

    def cadastrar_quarto(self):
        quarto = Room()
        quarto.setNumber(self.num_room.get())
        quarto.setName(self.name_room.get())
        quarto.setFloor(int(self.floor_room.get()))
        quarto.setDescription(self.desc_room.get())
        quarto.setDimension(float(self.dim_room.get()))
        quarto.setDailyRate(float(self.daily_room.get()))
        tipo_quarto = RoomType[self.type_room.get()]
        quarto.setRoomType(tipo_quarto)

        hostel = Hostel.getHostel()
        hostel.addRoom(quarto)

        print("Quarto cadastrado com sucesso!")

        mensagem = "Quarto cadastrado com sucesso!"
        messagebox.showinfo("Sucesso", mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    app = RoomCreationController(root)
    root.mainloop()
