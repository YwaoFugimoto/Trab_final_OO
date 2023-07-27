import tkinter as tk
from tkinter import ttk

def cadastra_room():
    numero = num_room.get()
    nome = name_room.get()
    andar = floor_room.get()
    descricao = desc_room.get()
    dimensao = dim_room.get()
    tipo = type_room.get()
    diaria = daily_room.get()


root = tk.Tk()
root.title("Cadastro de Quarto")
root.geometry("600x400")


label_numero = ttk.Label(root, text="Numero")
label_numero.place(x=15, y=30)

label_nome = ttk.Label(root, text="Nome")
label_nome.place(x=15, y=80)

label_andar = ttk.Label(root, text="Andar")
label_andar.place(x=15, y=130)

label_descricao = ttk.Label(root, text="Descriçao")
label_descricao.place(x=15, y=180)

label_dimensao = ttk.Label(root, text="Dimensao")
label_dimensao.place(x=15, y=230)

label_tipo = ttk.Label(root, text="Tipo")
label_tipo.place(x=15, y=280)

label_diaria = ttk.Label(root, text="Diaria")
label_diaria.place(x=15, y=330)

num_room = ttk.Entry(root)
num_room.place(x=415, y=25)

name_room = ttk.Entry(root)
name_room.place(x=415, y=75)

floor_room = ttk.Entry(root)
floor_room.place(x=415, y=125)

desc_room = ttk.Entry(root)
desc_room.place(x=415, y=175)

dim_room = ttk.Entry(root)
dim_room.place(x=415, y=225)

type_room = ttk.Combobox(root, values=["SINGLE", "DOUBLE", "EXECUTIVE_SUITE"])
type_room.place(x=436, y=275)

daily_room = ttk.Entry(root)
daily_room.place(x=415, y=325)

btn_cadastrar = ttk.Button(root, text="Cadastrar", command=cadastra_room)
btn_cadastrar.place(x=259, y=360)

root.mainloop()
