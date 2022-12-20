package game;
import javax.swing.*;
import java.awt.*;
public class Window extends JFrame {
//    393E46
    private String backgroud_color = "#444444";
    public int num_cell = 25;

    public String getBackgroud_color() {
        return this.backgroud_color;
    }

    public void setBackgroud_color(String backgroud_color) {
        this.backgroud_color = backgroud_color;
    }

    public Window() {
        JPanel p = new JPanel();
        JLabel[] b = new Ball[this.num_cell];
        p.setLayout(new GridLayout(5, 5, 7, 7));
        p.setBackground(Color.decode(this.backgroud_color));
        for (int i = 0; i < this.num_cell; i++) {
            b[i] = new Ball();
            p.add(b[i]);
        }
        add(p);
    }
}