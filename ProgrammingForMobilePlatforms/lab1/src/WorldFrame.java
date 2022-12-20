import java.awt.*;
import java.awt.event.*;

class WorldFrame extends Frame {
    WorldFrame(String s) {
        super(s);
    }

    public void paint(Graphics g) {
        g.setFont(new Font("Serif", Font.ITALIC | Font.BOLD, 30));
        g.drawString("Hello, XXi century world!", 20, 100);
    }

    public static void main(String[] args) {
        Frame f = new WorldFrame("Здравствуй, мир XXI века!");
        f.setSize(400,150);
        f.setVisible(true);
        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent ev) {
                System.exit(0);
            }
        });
    }
}