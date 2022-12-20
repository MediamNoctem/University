//package javaapplication1;
//import javax.swing.*;
//public class Main {
//    public static void main(String[] args) {
//        JFrame f = new JFrame();
//        JLabel lab = new JLabel("Я метка 1");
//        JButton[] b = new JButton[4];
//
//        f.setSize(300, 200);
//        f.setLocation(500,200);
//
//        f.add(lab);
//
//        for (int i = 0; i < 4; i++) {
//            b[i] = new JButton("Кнопка " + i);
//            f.add(b[i]);
//        }
//        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
//        f.setVisible(true);
//    }
//}

package javaapplication1;
import javax.swing.*;
public class Main {
    public static void main(String[] args) {
        JFrame f = new JFrame();
        JPanel p = new JPanel();
        JButton[] b = new JButton[9];
        f.setSize(300, 200);
        f.setLocation(500,200);
        for (int i = 0; i < 9; i++) {
            b[i] = new JButton("Кнопка " + i);
            p.add(b[i]);
        }
        f.add(p);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setVisible(true);
    }
}
