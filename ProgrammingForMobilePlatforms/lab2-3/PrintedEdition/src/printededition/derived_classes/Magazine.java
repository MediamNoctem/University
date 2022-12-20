//package printededition.derived_classes;
public class Magazine extends PrintedEdition {
    private int num_issues;
    public int getNum_issues() {
        return num_issues;
    }
    public void setNum_issues(int num_issues) {
        this.num_issues = num_issues;
    }

    public Magazine(int circulation, String language, int number_of_pages, int num_issues) {
        super.setCirculation(circulation);
        super.setLanguage(language);
        super.setNumber_of_pages(number_of_pages);
        setNum_issues(num_issues);
    }
    @Override
    public int calc_cost(int bs, int stat) {
        return (bs + 50 * stat)/super.getCirculation();
    }
    @Override
    public String toString() {
        return super.getCirculation() + " " + super.getLanguage() + " " + super.getNumber_of_pages() + " " + getNum_issues();
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