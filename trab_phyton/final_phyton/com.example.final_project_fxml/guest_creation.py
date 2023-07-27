import tkinter as tk
from tkinter import ttk

def cadastra_guest():
    nome = guest_name.get()
    sobrenome = guest_sobrenome.get()
    endereco = guest_end.get()
    email = guest_mail.get()
    titulo = guest_title.get()
    data_nascimento = guest_date.get()
    zip_code = guest_zip.get()
    cidade = guest_cidade.get()
    estado = guest_estado.get()
    pais = guest_pais.get()


root = tk.Tk()
root.title("Cadastro de Hóspede")
root.geometry("600x400")

label_nome = ttk.Label(root, text="Nome:")
label_nome.place(x=15, y=35)

label_sobrenome = ttk.Label(root, text="Sobrenome:")
label_sobrenome.place(x=14, y=95)

label_endereco = ttk.Label(root, text="Endereço:")
label_endereco.place(x=15, y=145)

label_email = ttk.Label(root, text="E-mail:")
label_email.place(x=15, y=225)

label_titulo = ttk.Label(root, text="Titulo:")
label_titulo.place(x=15, y=270)

label_data_nascimento = ttk.Label(root, text="Data de nascimento:")
label_data_nascimento.place(x=15, y=325)

guest_name = ttk.Entry(root)
guest_name.place(x=230, y=30)

guest_sobrenome = ttk.Entry(root)
guest_sobrenome.place(x=230, y=90)

guest_end = ttk.Entry(root)
guest_end.place(x=87, y=140)

guest_mail = ttk.Entry(root)
guest_mail.place(x=86, y=220)

guest_title = ttk.Combobox(root, values=["MR", "MRS", "MISS", "MS", "DR"])
guest_title.place(x=436, y=270)

guest_date = ttk.Entry(root)
guest_date.place(x=388, y=320)

guest_zip = ttk.Entry(root)
guest_zip.place(x=443, y=175)

guest_cidade = ttk.Entry(root)
guest_cidade.place(x=375, y=140)

guest_estado = ttk.Entry(root)
guest_estado.place(x=87, y=175)

guest_pais = ttk.Entry(root)
guest_pais.place(x=260, y=175)

btn_cadastrar = ttk.Button(root, text="Cadastrar", command=cadastra_guest)
btn_cadastrar.place(x=259, y=350)

root.mainloop()
