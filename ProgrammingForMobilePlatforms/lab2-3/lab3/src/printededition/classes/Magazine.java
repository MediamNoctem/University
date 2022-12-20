package printededition.classes;
public class Magazine implements PrintedEdition {
    private int circulation;
    private String language;
    private int number_of_pages;
    private int num_issues;
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
    public int getNum_issues() {
        return num_issues;
    }
    public void setNum_issues(int num_issues) {
        this.num_issues = num_issues;
    }

    public Magazine(int circulation, String language, int number_of_pages, int num_issues) {
        setCirculation(circulation);
        setLanguage(language);
        setNumber_of_pages(number_of_pages);
        setNum_issues(num_issues);
    }

    @Override
    public int calc_cost(int bs, int stat) {
        return (bs + 50 * stat)/getCirculation();
    }

    @Override
    public String toString() {
        return getCirculation() + " " + getLanguage() + " " + getNumber_of_pages() + " " + getNum_issues();
    }

    @Override
    public boolean equals(Object object) {
        boolean result = false;
        if (object != null && object instanceof Magazine) {
            Magazine mg = (Magazine)object;
            if (mg.getCirculation() == getCirculation() && mg.getLanguage() == getLanguage() && mg.getNumber_of_pages() == getNumber_of_pages() && mg.getNum_issues() == getNum_issues())
                result = true;
        }
        return result;
    }
}