package hostelapp.model;

public enum RoomType {
    SINGLE ("Single"),
    DOUBLE ("Double"),
    EXECUTIVE_SUITE ("Executive Suite");

    private final String roomType;

    private RoomType (String roomType){
            this.roomType = roomType;
    }

    public String getRoomType(){
        return roomType;
    }

}
