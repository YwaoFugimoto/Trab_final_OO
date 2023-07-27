import tkinter as tk
from tkinter import ttk

def open_hostel_info():
    hostel_info_window = tk.Toplevel()

    from hostel_info import GuestCreationInterface
    GuestCreationInterface(hostel_info_window)

    pass

def open_guest_creation():
    guest_creation_window = tk.Toplevel()

    from guest_creation import GuestCreationInterface
    GuestCreationInterface(guest_creation_window)


    pass

def open_room_creation():
    room_creation_window = tk.Toplevel()
    from room_creation import GuestCreationInterface
    GuestCreationInterface(room_creation_window)
    pass

def open_guest_list():
    guest_list_window = tk.Toplevel()
    from guest_list import GuestCreationInterace
    GuestCreationInterace(guest_list_window)

    pass

def atualizar_info():
    pass

root = tk.Tk()
root.title("Main Menu")
root.geometry("656x727")

frame = ttk.Frame(root, padding=(20, 20, 20, 20))
frame.pack(fill=tk.BOTH, expand=True)

hostel_info_button = ttk.Button(frame, text="Hostel Info", command=open_hostel_info)
hostel_info_button.pack()

guest_creation_button = ttk.Button(frame, text="Cadastrar Hospede", command=open_guest_creation)
guest_creation_button.pack()

room_creation_button = ttk.Button(frame, text="Cadastrar Quarto", command=open_room_creation)
room_creation_button.pack()

guest_list_button = ttk.Button(frame, text="Lista de Hospedes", command=open_guest_list)
guest_list_button.pack()

hostel_name_label = ttk.Label(frame, text="Nome do Hostel")
hostel_name_label.pack()

atualizar_button = ttk.Button(frame, text="Atualizar", command=atualizar_info)
atualizar_button.pack()

desc_label = ttk.Label(frame, text="Descrição")
desc_label.pack()

end_label = ttk.Label(frame, text="Endereço")
end_label.pack()

date_label = ttk.Label(frame, text="Data")
date_label.pack()

frame.pack(pady=20, padx=20)

root.mainloop()
