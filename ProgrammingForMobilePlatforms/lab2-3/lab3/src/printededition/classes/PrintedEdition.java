package printededition.classes;
public interface PrintedEdition {
    public int getCirculation();
    public void setCirculation(int circulation);
    public String getLanguage();
    public void setLanguage(String language);
    public int getNumber_of_pages();
    public void setNumber_of_pages(int number_of_pages);
    public abstract int calc_cost(int arg1, int arg2);
    public String toString();
}