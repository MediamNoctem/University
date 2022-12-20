package printededition.classes;
public class Newspaper implements PrintedEdition {
    private int circulation;
    private String language;
    private int number_of_pages;
    private String type;
    @Override
    public int getCirculation() {
        return circulation;
    }
    @Override
    public void setCirculation(int circulation) {
        this.circulation = circulation;
    }
    @Override
    public String getLanguage() {
        return language;
    }
    @Override
    public void setLanguage(String language) {
        this.language = language;
    }
    @Override
    public int getNumber_of_pages() {
        return number_of_pages;
    }
    @Override
    public void setNumber_of_pages(int number_of_pages) {
        this.number_of_pages = number_of_pages;
    }
    public String getType() {
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }

    public Newspaper(int circulation, String language, int number_of_pages, String type) {
        setCirculation(circulation);
        setLanguage(language);
        setNumber_of_pages(number_of_pages);
        setType(type);
    }

    @Override
    public int calc_cost(int bs, int str) {
        return (bs + 5 * str)/getCirculation();
    }

    @Override
    public String toString() {
        return getCirculation() + " " + getLanguage() + " " + getNumber_of_pages() + " " + getType();
    }

    @Override
    public boolean equals(Object object) {
        boolean result = false;
        if (object != null && object instanceof Newspaper) {
            Newspaper np = (Newspaper)object;
            if (np.getCirculation() == getCirculation() && np.getLanguage() == getLanguage() && np.getNumber_of_pages() == getNumber_of_pages() && np.getType() == getType())
                result = true;
        }
        return result;
    }
}