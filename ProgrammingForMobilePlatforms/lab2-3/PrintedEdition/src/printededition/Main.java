//package printededition;
import printededition.derived_classes.PrintedEdition;
import printededition.derived_classes.Newspaper;
import printededition.derived_classes.Magazine;
import printededition.derived_classes.Book;
public class Main {
    public static void main(String[] args) {
        PrintedEdition[] pe = new PrintedEdition[3];
        pe[0] = new Newspaper(5000, "rus", 60, "printed");
        pe[1] = new Magazine(5000, "rus", 90, 50000);
        pe[2] = new Book(5000, "en", 880, "Joyce");

        System.out.println(pe[0].calc_cost(5000,1000));
        System.out.println(pe[1].calc_cost(15000,100));
        System.out.println(pe[2].calc_cost(1500,1));

        Newspaper np = new Newspaper(5000, "rus", 60, "printed");
        System.out.println(pe[0].equals(pe[1]));
        System.out.println(pe[0].equals(np));

        System.out.println(pe[0].toString());
        System.out.println(pe[1].toString());
        System.out.println(pe[2].toString());
    }
}