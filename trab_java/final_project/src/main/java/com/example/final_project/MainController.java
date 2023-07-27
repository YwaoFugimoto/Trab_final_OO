package com.example.final_project;

import hostelapp.model.Address;
import hostelapp.model.Hostel;
import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.event.ActionEvent;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;

public class MainController{

    private final String FILE_PATH = "hostel_info.dat";

    @FXML private Label hostel_name;
    @FXML private Label desc_label;
    @FXML private Label end_label;
    @FXML private Label date_label;

    private Hostel hostel;

    @FXML
    public void initialize() {
        hostel = readHostelFromFile();
        if (hostel != null) {
            hostel_name.setText(hostel.getName());
            desc_label.setWrapText(true);
            desc_label.setText(hostel.getDescription());
            end_label.setText(toString(hostel.getAddress()));
            String data = hostel.getInaugurationDate().toString();
            date_label.setText("Desde: " + data);
        }
    }


    public void atulizar_info(){
        Hostel hostel = Hostel.getHostel();
        hostel_name.setText(hostel.getName());
        desc_label.setWrapText(true);
        desc_label.setText(hostel.getDescription());
        end_label.setText(toString(hostel.getAddress()));
        String data = hostel.getInaugurationDate().toString();
        date_label.setText("Desde: " + data);
    }

    private String toString(Address address) {
        return "Endereco: " + address.getAddress() + "\nZip-Code:" + address.getZipCode()
                + "\nCidade: " + address.getCity() + "\nEstado: " + address.getState()
                + "\nPais: " + address.getCountry();
    }

    public void openGuestCreation (ActionEvent event) throws Exception {
        Parent newInterfaceView = FXMLLoader.load(getClass().getResource("guest_creation.fxml"));

        Stage newInterfaceStage = new Stage();
        newInterfaceStage.setTitle("Cadatro de Hospede");
        newInterfaceStage.setScene(new Scene(newInterfaceView));
        newInterfaceStage.show();
    }
    public void openGuestList (ActionEvent event) throws Exception {
        Parent newInterfaceView = FXMLLoader.load(getClass().getResource("guest_list.fxml"));

        Stage newInterfaceStage = new Stage();
        newInterfaceStage.setTitle("Lista de Hospedes");
        newInterfaceStage.setScene(new Scene(newInterfaceView));
        newInterfaceStage.show();
    }
    public void openHostelInfo (ActionEvent event) throws Exception {
        Parent newInterfaceView = FXMLLoader.load(getClass().getResource("hostel_info.fxml"));

        Stage newInterfaceStage = new Stage();
        newInterfaceStage.setTitle("Informações do Hostel");
        newInterfaceStage.setScene(new Scene(newInterfaceView));
        newInterfaceStage.show();
    }
    public void openRoomCreation (ActionEvent event) throws Exception {
        Parent newInterfaceView = FXMLLoader.load(getClass().getResource("room_creation.fxml"));

        Stage newInterfaceStage = new Stage();
        newInterfaceStage.setTitle("Cadatro de Quarto");
        newInterfaceStage.setScene(new Scene(newInterfaceView));
        newInterfaceStage.show();
    }

        public Hostel readHostelFromFile() {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(FILE_PATH))) {
                return (Hostel) ois.readObject();
            } catch (IOException | ClassNotFoundException e) {
                System.err.println("Error while reading hostel info from file: " + e.getMessage());
                return null;
            }
        }
}