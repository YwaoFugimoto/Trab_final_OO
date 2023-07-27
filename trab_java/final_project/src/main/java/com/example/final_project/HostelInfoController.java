package com.example.final_project;

import hostelapp.model.Address;
import hostelapp.model.Hostel;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.DatePicker;
import javafx.event.ActionEvent;
import javafx.scene.control.TextField;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.time.LocalDate;
import java.time.format.DateTimeParseException;

public class HostelInfoController {

    @FXML private TextField hostel_name;
    @FXML private TextField hostel_end;
    @FXML private TextField hostel_tel;
    @FXML private TextField hostel_mail;
    @FXML private TextField hostel_desc;
    @FXML private DatePicker hostel_date;
    @FXML private TextField hostel_zip;
    @FXML private TextField hostel_cidade;
    @FXML private TextField hostel_pais;
    @FXML private TextField hostel_estado;


    @FXML
    private void saveInfoButton (ActionEvent event){
        String nome = hostel_name.getText();
        String end = hostel_end.getText();
        String tel = hostel_tel.getText();
        String mail = hostel_mail.getText();
        String desc = hostel_desc.getText();
        LocalDate date = hostel_date.getValue();
        String zip = hostel_zip.getText();
        String cidade = hostel_cidade.getText();
        String pais = hostel_pais.getText();
        String estado = hostel_estado.getText();

        try {
            Address address = new Address();
            address.setZipCode(zip);
            address.setAddress(end);
            address.setCity(cidade);
            address.setCountry(pais);
            address.setState(estado);

            Hostel hostel = Hostel.getHostel();
            hostel.setName(nome);
            hostel.setAddress(address);
            hostel.setPhone(tel);
            hostel.setContactEmail(mail);
            hostel.setDescription(desc);
            hostel.setInaugurationDate(date);

            saveHostelInfo(hostel);

            System.out.println("As informações do albergue foram salvas com sucesso!");
        } catch (DateTimeParseException e) {
            System.err.println("Erro: Formato de data inválido. Use o formato dd/MM/yyyy.");
        } catch (IOException e) {
            System.err.println("Erro ao salvar as informações do albergue: " + e.getMessage());
        }

        String message = "Informações salvas com sucesso!";
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Sucesso");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();

    }
    private void saveHostelInfo(Hostel hostel) throws IOException {
        String filename = "hostel_info.dat";
        try (FileOutputStream fileOut = new FileOutputStream(filename);
             ObjectOutputStream objectOut = new ObjectOutputStream(fileOut)) {
            objectOut.writeObject(hostel);
        }
    }


}
