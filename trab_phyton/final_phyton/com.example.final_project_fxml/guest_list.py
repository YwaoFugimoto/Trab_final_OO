import tkinter as tk
from tkinter import ttk

def list_all_guests():
    guests = []  
    guest_list.delete(0, tk.END) 
    for guest in guests:
        guest_list.insert(tk.END, guest)  
        
root = tk.Tk()
root.title("Lista de Hóspedes")
root.geometry("600x469")

guest_list = tk.Listbox(root, height=20, width=80)
guest_list.place(x=0, y=37)

btn_atualizar = ttk.Button(root, text="Atualizar", command=list_all_guests)
btn_atualizar.place(x=507, y=420)

label_nome = ttk.Label(root, text="Nome")
label_nome.place(x=0, y=10)

label_sobrenome = ttk.Label(root, text="Sobrenome")
label_sobrenome.place(x=119, y=10)

label_email = ttk.Label(root, text="E-mail")
label_email.place(x=242, y=10)

root.mainloop()
