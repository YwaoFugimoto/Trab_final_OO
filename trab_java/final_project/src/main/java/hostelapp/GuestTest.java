package hostelapp;

import hostelapp.model.*;
import hostelapp.model.Date;

import java.time.LocalDate;
import java.util.List;

public class GuestTest {
    public static void main(String[] args) {

        String description = "The hostel Sparkling Water is located in a small town called Caxambu-MG";
        Hostel hostel = Hostel.getHostel();
        hostel.setName("Sparkling Water");
        hostel.setContactEmail("sparkling@gmail.com");
        hostel.setPhone("+(55)-35-3343-1234");
        hostel.setDescription(description);
        hostel.setContactEmail("sparkling-water@gmail.com");
        hostel.setInaugurationDate(LocalDate.of(2000, 5, 7));

        Address hostelAddress = new Address();
        hostelAddress.setAddress("Rua Camilo Soares");
        hostelAddress.setCity("Caxambu");
        hostelAddress.setState("MG");
        hostelAddress.setCountry("Brazil");
        hostelAddress.setZipCode("123400-000");

        hostel.setAddress(hostelAddress);

        System.out.println("Printing hostel details:");
        System.out.println(hostel.toString());
        System.out.println();

        Guest florentino = new Guest();
        florentino.setTitle(Title.MS);
        florentino.setName("Florentino");
        florentino.setLastName("Ariza");
        florentino.setEmail("ariza@gmail.com");

        Date birthday = new Date();
        birthday.setDay(35);
        birthday.setMonth(2);
        birthday.setYear(1970);

        florentino.setBirthDate(birthday);

        Address address = new Address();
        address.setAddress("Rua Joaquim Lázaro Gomes");
        address.setCity("Alfenas");
        address.setZipCode("37130-000");
        address.setState("MG");
        address.setCountry("Brazil");

        florentino.setAddress(address);


        Reservation reservation1 = new Reservation();
        Date reservationDate1 = new Date(12, 5, 2023);
        Date checkinDate1 = new Date(15, 7, 2023);
        Date checkoutDate1 = new Date(22, 7, 2023);
        reservation1.setReservationDate(reservationDate1);
        reservation1.setCheckinDate(checkinDate1);
        reservation1.setCheckoutDate(checkoutDate1);

        Reservation reservation2 = new Reservation();
        Date reservationDate2 = new Date(10, 2, 2023);
        Date checkinDate2 = new Date(20, 8, 2023);
        Date checkoutDate2 = new Date(23, 8, 2023);
        reservation2.setReservationDate(reservationDate2);
        reservation2.setCheckinDate(checkinDate2);
        reservation2.setCheckoutDate(checkoutDate2);

//        ArrayList<Reservation> reservations = new ArrayList<>();
//        reservations.add(reservation1);
//        reservations.add(reservation2);

//        florentino.setReservations(reservations);

        florentino.addReservation(reservation1);
        florentino.addReservation(reservation2);

        Address florentinoAddress = florentino.getAddress();
        String city = florentinoAddress.getCity();

        System.out.println("Title...: " + florentino.getTitle());
        System.out.println("Name...: " + florentino.getFirstName());
        System.out.println("Last name...: " + florentino.getLastName());
        System.out.println("Email...: " + florentino.getEmail());
        System.out.println("Birthdate..: " + florentino.getBirthDate());
        System.out.println("Address...: " + florentino.getAddress().getAddress());
        System.out.println("City....: " + city);
        System.out.println("State...: " + florentino.getAddress().getState());
        System.out.println("Zip Code..: " + florentino.getAddress().getZipCode());
        System.out.println("Country..: " + florentino.getAddress().getCountry());

        List<Reservation> temp = florentino.getReservations();
        for (Reservation reservation: temp){
            System.out.println(reservation);
        }


        Guest fermina = new Guest();
        fermina.setName("Fermina");
        fermina.setLastName("Daza");

        Guest atticus = new Guest("Atticus", "Finch");

        Guest gregor = new Guest("Gregor");
        gregor.setLastName("Samsa");

        System.out.println();
        System.out.println("Name...: " + fermina.getFirstName());
        System.out.println("Last name...: " + fermina.getLastName());

        System.out.println();
        System.out.println("Name...: " + atticus.getFirstName());
        System.out.println("Last name...: " + atticus.getLastName());

        System.out.println();
        System.out.println("Name...: " + gregor.getFirstName());
        System.out.println("Last name...: " + gregor.getLastName());

    }
}
