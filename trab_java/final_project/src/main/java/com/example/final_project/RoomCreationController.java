package com.example.final_project;

import hostelapp.model.Hostel;
import hostelapp.model.Room;
import hostelapp.model.RoomType;
import javafx.fxml.FXML;
import javafx.scene.control.Alert;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.TextField;

public class RoomCreationController {


    @FXML private TextField num_room;
    @FXML private TextField name_room;
    @FXML private TextField floor_room;
    @FXML private TextField desc_room;
    @FXML private TextField dim_room;
    @FXML private TextField daily_room;
    @FXML private ChoiceBox type_room;

    public void cadastra_room(){
        Room room = new Room();
        room.setNumber(num_room.getText());
        room.setName(name_room.getText());
        room.setFloor(Integer.parseInt(floor_room.getText()));
        room.setDescription(desc_room.getText());
        room.setDimension(Double.parseDouble(dim_room.getText()));
        room.setDailyRate(Double.parseDouble(daily_room.getText()));
        String s_typeRoom = (String) type_room.getValue();
        RoomType roomType = RoomType.valueOf(s_typeRoom);
        room.setRoomType(roomType);
        Hostel hostel = Hostel.getHostel();
        hostel.addRoom(room);


        System.out.println("Quarto cadastrado com sucesso!");

        String message = "Quarto cadastrado com sucesso!";
        Alert alert = new Alert(Alert.AlertType.INFORMATION);
        alert.setTitle("Sucesso");
        alert.setHeaderText(null);
        alert.setContentText(message);
        alert.showAndWait();
    }








}
