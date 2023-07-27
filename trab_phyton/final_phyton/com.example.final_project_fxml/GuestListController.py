import pickle
from hostelapp.model import Guest, Hostel
from tkinter import Listbox

class GuestListController:
    def __init__(self):
        self.guest_list = Listbox()  

        self.FILE_PATH = "guests.dat"

        self.loadGuestsFromFile()

    def loadGuestsFromFile(self):
        try:
            with open(self.FILE_PATH, "rb") as file:
                guests = pickle.load(file)
                self.guest_list.delete(0, 'end')
                for guest in guests:
                    self.guest_list.insert('end', guest)
        except (IOError, pickle.UnpicklingError) as e:
            print("Erro ao carregar hóspedes do arquivo:", e)

    def saveGuestsToFile(self):
        hostel = Hostel.getHostel()
        guests = hostel.getAllGuests()

        try:
            with open(self.FILE_PATH, "wb") as file:
                pickle.dump(guests, file)
        except IOError as e:
            print("Erro ao salvar hóspedes no arquivo:", e)

    def listarTodosHospedes(self):
        hostel = Hostel.getHostel()
        lista_hospedes = hostel.getAllGuests()
        self.guest_list.delete(0, 'end')
        for guest in lista_hospedes:
            self.guest_list.insert('end', guest)
        self.saveGuestsToFile()
