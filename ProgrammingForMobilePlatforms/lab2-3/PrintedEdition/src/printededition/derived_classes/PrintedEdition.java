//package printededition.derived_classes;
public abstract class PrintedEdition {
    private int circulation;
    private String language;
    private int number_of_pages;

    public int getCirculation() {
        return circulation;
    }
    public void setCirculation(int circulation) {
        this.circulation = circulation;
    }
    public String getLanguage() {
        return language;
    }
    public void setLanguage(String language) {
        this.language = language;
    }
    public int getNumber_of_pages() {
        return number_of_pages;
    }
    public void setNumber_of_pages(int number_of_pages) {
        this.number_of_pages = number_of_pages;
    }

    public abstract int calc_cost(int arg1, int arg2);
    @Override
    public String toString() {
        return getCirculation() + " " + getLanguage() + " " + getNumber_of_pages();
    }
}