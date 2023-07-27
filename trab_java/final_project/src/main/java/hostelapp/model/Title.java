package hostelapp.model;

public enum Title {
    MR("Mr."),
    MRS("Mrs."),
    MISS("Miss"),
    MS("Ms."),
    DR("Dr.");

    private final String title;

    private Title(String title) {
        this.title = title;
    }

    public String getTitle() {
        return title;
    }
}