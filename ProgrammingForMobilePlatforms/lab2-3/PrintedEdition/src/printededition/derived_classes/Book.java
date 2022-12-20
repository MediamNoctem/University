//package printededition.derived_classes;
public class Book extends PrintedEdition {
    private String author;
    public String getAuthor() {
        return author;
    }
    public void setAuthor(String author) {
        this.author = author;
    }
    public Book(int circulation, String language, int number_of_pages, String author) {
        super.setCirculation(circulation);
        super.setLanguage(language);
        super.setNumber_of_pages(number_of_pages);
        setAuthor(author);
    }
    @Override
    public int calc_cost(int bs, int str) {
        return (bs + 500 * str);
    }
    @Override
    public String toString() {
        return super.getCirculation() + " " + super.getLanguage() + " " + super.getNumber_of_pages() + " " + getAuthor();
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