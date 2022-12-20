package printededition.classes;
public class Book implements PrintedEdition {
    private int circulation;
    private String language;
    private int number_of_pages;
    private String author;
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
    public String getAuthor() {
        return author;
    }
    public void setAuthor(String author) {
        this.author = author;
    }

    public Book(int circulation, String language, int number_of_pages, String author) {
        setCirculation(circulation);
        setLanguage(language);
        setNumber_of_pages(number_of_pages);
        setAuthor(author);
    }

    @Override
    public int calc_cost(int bs, int str) {
        return (bs + 500 * str);
    }

    @Override
    public String toString() {
        return getCirculation() + " " + getLanguage() + " " + getNumber_of_pages() + " " + getAuthor();
    }

    @Override
    public boolean equals(Object object) {
        boolean result = false;
        if (object != null && object instanceof Book) {
            Book bk = (Book)object;
            if (bk.getCirculation() == getCirculation() && bk.getLanguage() == getLanguage() && bk.getNumber_of_pages() == getNumber_of_pages() && bk.getAuthor() == getAuthor())
                result = true;
        }
        return result;
    }
}