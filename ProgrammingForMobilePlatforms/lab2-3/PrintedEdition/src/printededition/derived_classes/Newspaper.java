//package printededition.derived_classes;
public class Newspaper extends PrintedEdition {
    private String type;
    public String getType() {
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }

    public Newspaper(int circulation, String language, int number_of_pages, String type) {
        super.setCirculation(circulation);
        super.setLanguage(language);
        super.setNumber_of_pages(number_of_pages);
        setType(type);
    }
    @Override
    public int calc_cost(int bs, int str) {
        return (bs + 5 * str)/super.getCirculation();
    }
    @Override
    public String toString() {
        return super.getCirculation() + " " + super.getLanguage() + " " + super.getNumber_of_pages() + " " + getType();
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