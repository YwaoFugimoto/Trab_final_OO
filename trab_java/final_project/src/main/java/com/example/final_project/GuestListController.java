package com.example.final_project;

import hostelapp.model.Guest;
import hostelapp.model.Hostel;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.ListView;
import java.io.*;
import java.util.List;

public class GuestListController {

    @FXML
    private ListView<Guest> guest_list;

    private final String FILE_PATH = "guests.dat";

    public void loadGuestsFromFile() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(FILE_PATH))) {
            List<Guest> guests = (List<Guest>) ois.readObject();
            ObservableList<Guest> observableList = FXCollections.observableArrayList(guests);
            guest_list.setItems(observableList);
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Error while loading guests from file: " + e.getMessage());
        }
    }

    public void saveGuestsToFile() {
        Hostel hostel = Hostel.getHostel();
        List<Guest> guests = hostel.getAllGuests();

        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FILE_PATH))) {
            oos.writeObject(guests);
        } catch (IOException e) {
            System.err.println("Error while saving guests to file: " + e.getMessage());
        }
    }


    @FXML public void initialize(){
        loadGuestsFromFile();
    }

    public void listAllGuest(){
        Hostel hostel = Hostel.getHostel();
        List<Guest> lista = hostel.getAllGuests();
        ObservableList<Guest> observableList = FXCollections.observableArrayList(lista);
        guest_list.setItems(observableList);
        saveGuestsToFile();
    }



}