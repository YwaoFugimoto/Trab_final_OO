package com.example.final_project;

import hostelapp.model.*;
import javafx.fxml.FXML;
import javafx.scene.control.*;

public class GuestCreationController {

    @FXML private TextField guest_name;
    @FXML private TextField guest_sobrenome;
    @FXML private TextField guest_end;
    @FXML private TextField guest_mail;
    @FXML private TextField guest_cidade;
    @FXML private TextField guest_estado;
    @FXML private TextField guest_zip;
    @FXML private TextField guest_pais;
    @FXML private DatePicker guest_date;
    @FXML private ChoiceBox guest_title;


    public void cadastra_guest(){
        Guest guest = new Guest();
        guest.setName(guest_name.getText());
        guest.setLastName(guest_sobrenome.getText());
        Address guest_address = new Address();
        guest_address.setCity(guest_cidade.getText());
        guest_address.setCountry(guest_pais.getText());
        guest_address.setState(guest_estado.getText());
        guest_address.setZipCode(guest_zip.getText());
        guest_address.setAddress(guest_end.getText());
        guest.setAddress(guest_address);
        guest.setEmail(guest_mail.getText());
        Date data = new Date();
        data.setDay(guest_date.getValue().getDayOfMonth());
        data.setMonth(guest_date.getValue().getMonthValue());
        data.setYear(guest_date.getValue().getYear());
        guest.setBirthDate(data);
        String s_title = (String)guest_title.getValue();
        Title title = Title.valueOf(s_title);
        guest.setTitle(title);
        Hostel hostel = Hostel.getHostel();
        hostel.addGuest(guest);

        System.out.println("Hóspede cadastrado com sucesso!");

        String message = "Hóspede cadastrado com sucesso!";
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Sucesso");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();

    }
}
