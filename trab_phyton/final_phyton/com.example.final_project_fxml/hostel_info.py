import tkinter as tk
from tkinter import ttk

def save_info():
    nome = hostel_name.get()
    endereco = hostel_end.get()
    zip_code = hostel_zip.get()
    cidade = hostel_cidade.get()
    estado = hostel_estado.get()
    pais = hostel_pais.get()
    telefone = hostel_tel.get()
    email = hostel_mail.get()
    descricao = hostel_desc.get("1.0", tk.END)
    inauguracao = hostel_date.get()


root = tk.Tk()
root.title("Informações do Hostel")
root.geometry("600x400")

label_nome = ttk.Label(root, text="Nome:")
label_nome.place(x=10, y=30)

label_endereco = ttk.Label(root, text="Endereço:")
label_endereco.place(x=10, y=60)

label_zip = ttk.Label(root, text="Zip code:")
label_zip.place(x=10, y=90)

label_cidade = ttk.Label(root, text="Cidade:")
label_cidade.place(x=10, y=120)

label_estado = ttk.Label(root, text="Estado:")
label_estado.place(x=10, y=155)

label_pais = ttk.Label(root, text="Pais:")
label_pais.place(x=10, y=185)

label_telefone = ttk.Label(root, text="Telefone:")
label_telefone.place(x=10, y=215)

label_email = ttk.Label(root, text="E-mail:")
label_email.place(x=10, y=253)

label_descricao = ttk.Label(root, text="Descrição:")
label_descricao.place(x=10, y=284)

label_inauguracao = ttk.Label(root, text="Inauguração:")
label_inauguracao.place(x=10, y=341)

hostel_name = ttk.Entry(root)
hostel_name.place(x=196, y=26)

hostel_end = ttk.Entry(root)
hostel_end.place(x=196, y=55)

hostel_zip = ttk.Entry(root)
hostel_zip.place(x=196, y=85)

hostel_cidade = ttk.Entry(root)
hostel_cidade.place(x=196, y=115)

hostel_estado = ttk.Entry(root)
hostel_estado.place(x=196, y=150)

hostel_pais = ttk.Entry(root)
hostel_pais.place(x=196, y=180)

hostel_tel = ttk.Entry(root)
hostel_tel.place(x=196, y=210)

hostel_mail = ttk.Entry(root)
hostel_mail.place(x=196, y=248)

hostel_desc = tk.Text(root, width=48, height=3)
hostel_desc.place(x=196, y=284)

hostel_date = ttk.DatePicker(root)
hostel_date.place(x=388, y=336)

btn_salvar = ttk.Button(root, text="Salvar", command=save_info)
btn_salvar.place(x=269, y=360)

root.mainloop()
