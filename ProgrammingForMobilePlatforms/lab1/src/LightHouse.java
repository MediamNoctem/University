import java.awt.*;
import java.awt.event.*;

public class LightHouse extends Frame {
    LightHouse(String s) {
        super(s);
        setBounds(0,0,850,850);
        setVisible(true);
    }
    public void paint(Graphics g) {
        Dimension d = getSize();
        int myWidth = 755, myHeight = 755, size_pixel = 5;

        // Небо и море
        g.setColor(new Color(88, 72, 109));
        g.fillRect((d.width - myWidth)/2, myHeight + (d.height - myHeight)/2 - size_pixel * 65, size_pixel * 151, size_pixel * 65);
        g.setColor(new Color(155, 146, 167));
        g.fillRect((d.width - myWidth)/2, (d.height - myHeight)/2, size_pixel * 151, size_pixel * 86);

        // Прорисовка моря
        g.setColor(new Color(107, 91, 128));

        g.fillRect((d.width - myWidth)/2 + size_pixel * 36, myHeight + (d.height - myHeight)/2 - size_pixel, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 50, myHeight + (d.height - myHeight)/2 - size_pixel, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 53, myHeight + (d.height - myHeight)/2 - size_pixel, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 106, myHeight + (d.height - myHeight)/2 - size_pixel, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 116, myHeight + (d.height - myHeight)/2 - size_pixel, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 32, myHeight + (d.height - myHeight)/2 - size_pixel * 2, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 2, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 109, myHeight + (d.height - myHeight)/2 - size_pixel * 2, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 115, myHeight + (d.height - myHeight)/2 - size_pixel * 2, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 124, myHeight + (d.height - myHeight)/2 - size_pixel * 2, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 138, myHeight + (d.height - myHeight)/2 - size_pixel * 2, size_pixel * 9, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 23, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 26, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 33, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 77, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 80, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 83, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 101, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 111, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 113, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 118, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 123, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 130, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 136, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 147, myHeight + (d.height - myHeight)/2 - size_pixel * 3, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 30, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 14, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 58, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 60, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 78, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel * 9, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 96, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 121, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 134, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 148, myHeight + (d.height - myHeight)/2 - size_pixel * 4, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 12, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 14, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 18, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 24, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 56, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 18, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 80, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 91, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 93, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 5, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 27, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 54, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 81, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 84, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 94, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 3, size_pixel);

        // Камни
        g.setColor(new Color(45, 37, 14));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 105, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel * 21, size_pixel * 11);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 108, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 28, size_pixel * 12);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 126, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel * 4, size_pixel * 7);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 130, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 3, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 133, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel * 2, size_pixel * 3);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 133, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel * 15, size_pixel * 8);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 148, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 136, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel * 11, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 114, myHeight + (d.height - myHeight)/2 - size_pixel * 8, size_pixel * 9, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 108, myHeight + (d.height - myHeight)/2 - size_pixel * 7, size_pixel * 12, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 109, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 107, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 107, myHeight + (d.height - myHeight)/2 - size_pixel * 6, size_pixel, size_pixel);

        g.setColor(new Color(43, 46, 37));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 146, myHeight + (d.height - myHeight)/2 - size_pixel * 11, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 146, myHeight + (d.height - myHeight)/2 - size_pixel * 12, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 141, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 141, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 140, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 135, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel * 7, size_pixel);


        g.setColor(new Color(104, 71, 52));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 30, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 29, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 28, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 33, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 30, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 34, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 31, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 33, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 32, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 32, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 34, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 35, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 37, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 8, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 42, myHeight + (d.height - myHeight)/2 - size_pixel * 24, size_pixel * 4, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 39, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel * 5, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 38, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 40, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 37, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel * 7, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 40, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 65, size_pixel * 9);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 76, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 30, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 94, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 12, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 97, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 11, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 104, myHeight + (d.height - myHeight)/2 - size_pixel * 11, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 50, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 12, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 54, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 8, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 66, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 49, myHeight + (d.height - myHeight)/2 - size_pixel * 38, size_pixel * 23, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 47, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel * 11, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 66, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 4, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 126, myHeight + (d.height - myHeight)/2 - size_pixel * 8, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 130, myHeight + (d.height - myHeight)/2 - size_pixel * 9, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 131, myHeight + (d.height - myHeight)/2 - size_pixel * 11, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 131, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 129, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 127, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 126, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 125, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 123, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 121, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 81, myHeight + (d.height - myHeight)/2 - size_pixel * 43, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 83, myHeight + (d.height - myHeight)/2 - size_pixel * 44, size_pixel * 2, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 85, myHeight + (d.height - myHeight)/2 - size_pixel * 43, size_pixel * 3, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 88, myHeight + (d.height - myHeight)/2 - size_pixel * 43, size_pixel * 3, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 92, myHeight + (d.height - myHeight)/2 - size_pixel * 42, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 94, myHeight + (d.height - myHeight)/2 - size_pixel * 42, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 96, myHeight + (d.height - myHeight)/2 - size_pixel * 41, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 55, myHeight + (d.height - myHeight)/2 - size_pixel * 45, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 57, myHeight + (d.height - myHeight)/2 - size_pixel * 47, size_pixel * 2, size_pixel * 2);

        g.setColor(new Color(172, 109, 102));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 29, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 28, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 28, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 29, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 31, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 31, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 32, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel * 3, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 37, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 38, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 38, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 39, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 41, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 37, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 38, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 40, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 43, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 41, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 41, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 40, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 47, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 48, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 50, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 42, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 51, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 52, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 53, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 47, myHeight + (d.height - myHeight)/2 - size_pixel * 37, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 49, myHeight + (d.height - myHeight)/2 - size_pixel * 38, size_pixel * 4, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 12, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 65, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 66, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel, size_pixel * 2);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 51, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 53, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 57, myHeight + (d.height - myHeight)/2 - size_pixel * 24, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 52, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 52, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 54, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 57, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 65, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 76, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 77, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 76, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 77, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 75, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 76, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 77, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel, size_pixel);

        g.setColor(new Color(61, 49, 33));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 29, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 32, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 28, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 35, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 34, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 33, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 32, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 31, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 35, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 35, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 35, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 35, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 36, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 41, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 42, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 46, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 45, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 24, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 53, myHeight + (d.height - myHeight)/2 - size_pixel * 38, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 53, myHeight + (d.height - myHeight)/2 - size_pixel * 39, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 56, myHeight + (d.height - myHeight)/2 - size_pixel * 40, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 55, myHeight + (d.height - myHeight)/2 - size_pixel * 42, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 55, myHeight + (d.height - myHeight)/2 - size_pixel * 43, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 56, myHeight + (d.height - myHeight)/2 - size_pixel * 44, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 38, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 41, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 44, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 43, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 41, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 42, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 45, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 5, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 50, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 46, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 47, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 49, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 50, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 51, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 52, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 54, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 54, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 55, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel * 8, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 55, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 59, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 60, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 59, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 61, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 10, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 65, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 37, size_pixel * 3, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel * 3, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 3, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 74, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 24, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 65, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 61, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 58, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel * 3, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 57, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 56, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 55, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 53, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 52, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 54, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 52, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 51, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 50, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 61, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel * 4);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 75, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel, size_pixel * 2);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 75, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel * 5, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 79, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 84, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 83, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 10, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 9, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 10, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel * 4, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 3, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel * 5, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel * 6, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 68, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 65, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 66, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 67, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 76, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 77, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 81, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 82, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 86, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 87, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 88, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 87, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 2, size_pixel * 13);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 84, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 3, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 86, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel, size_pixel * 11);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 85, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel, size_pixel * 10);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 89, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 90, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel * 7);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 91, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel * 2, size_pixel * 7);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 90, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 93, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 93, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 4, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 94, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 93, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 95, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel * 9);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 96, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel, size_pixel * 9);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 97, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel, size_pixel * 8);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 98, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel * 10);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 99, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 100, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 101, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 102, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel, size_pixel * 7);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 104, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel, size_pixel * 12);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 105, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel, size_pixel * 10);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 106, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 106, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel, size_pixel * 10);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 107, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel, size_pixel * 9);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 108, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel, size_pixel * 12);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 106, myHeight + (d.height - myHeight)/2 - size_pixel * 12, size_pixel * 2, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 106, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 105, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 109, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel, size_pixel * 9);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 110, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel, size_pixel * 8);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 111, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel * 2, size_pixel * 7);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 113, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 114, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 115, myHeight + (d.height - myHeight)/2 - size_pixel * 11, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 116, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 115, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 114, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 113, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 112, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 111, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 110, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 110, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 102, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 102, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 104, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 105, myHeight + (d.height - myHeight)/2 - size_pixel * 19, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 105, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel, size_pixel * 2);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 105, myHeight + (d.height - myHeight)/2 - size_pixel * 11, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 7, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 100, myHeight + (d.height - myHeight)/2 - size_pixel * 11, size_pixel * 4, size_pixel * 2);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 97, myHeight + (d.height - myHeight)/2 - size_pixel * 13, size_pixel * 3, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 96, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 97, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 98, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 94, myHeight + (d.height - myHeight)/2 - size_pixel * 17, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 93, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 93, myHeight + (d.height - myHeight)/2 - size_pixel * 21, size_pixel, size_pixel * 4);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 120, myHeight + (d.height - myHeight)/2 - size_pixel * 12, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 121, myHeight + (d.height - myHeight)/2 - size_pixel * 15, size_pixel, size_pixel * 2);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 125, myHeight + (d.height - myHeight)/2 - size_pixel * 9, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 128, myHeight + (d.height - myHeight)/2 - size_pixel * 8, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 131, myHeight + (d.height - myHeight)/2 - size_pixel * 8, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 134, myHeight + (d.height - myHeight)/2 - size_pixel * 9, size_pixel, size_pixel * 3);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 129, myHeight + (d.height - myHeight)/2 - size_pixel * 9, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 130, myHeight + (d.height - myHeight)/2 - size_pixel * 10, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 131, myHeight + (d.height - myHeight)/2 - size_pixel * 12, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 130, myHeight + (d.height - myHeight)/2 - size_pixel * 14, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 128, myHeight + (d.height - myHeight)/2 - size_pixel * 16, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 127, myHeight + (d.height - myHeight)/2 - size_pixel * 18, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 125, myHeight + (d.height - myHeight)/2 - size_pixel * 20, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 124, myHeight + (d.height - myHeight)/2 - size_pixel * 22, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 122, myHeight + (d.height - myHeight)/2 - size_pixel * 24, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 120, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 119, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 117, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 116, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 114, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 113, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 112, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 108, myHeight + (d.height - myHeight)/2 - size_pixel * 37, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 107, myHeight + (d.height - myHeight)/2 - size_pixel * 38, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 105, myHeight + (d.height - myHeight)/2 - size_pixel * 39, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 40, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 98, myHeight + (d.height - myHeight)/2 - size_pixel * 41, size_pixel * 5, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 132, myHeight + (d.height - myHeight)/2 - size_pixel * 23, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 130, myHeight + (d.height - myHeight)/2 - size_pixel * 24, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 132, myHeight + (d.height - myHeight)/2 - size_pixel * 24, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 129, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 131, myHeight + (d.height - myHeight)/2 - size_pixel * 25, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 128, myHeight + (d.height - myHeight)/2 - size_pixel * 26, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 129, myHeight + (d.height - myHeight)/2 - size_pixel * 27, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 126, myHeight + (d.height - myHeight)/2 - size_pixel * 28, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 125, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 126, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 125, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 124, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 124, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 59, myHeight + (d.height - myHeight)/2 - size_pixel * 47, size_pixel * 2, size_pixel * 2);

        g.setColor(new Color(45, 37, 14));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 41, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 43, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 46, myHeight + (d.height - myHeight)/2 - size_pixel * 37, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 47, myHeight + (d.height - myHeight)/2 - size_pixel * 38, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 57, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 58, myHeight + (d.height - myHeight)/2 - size_pixel * 37, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 62, myHeight + (d.height - myHeight)/2 - size_pixel * 37, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 60, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 85, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 86, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 88, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 89, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel * 11, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 91, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 91, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 95, myHeight + (d.height - myHeight)/2 - size_pixel * 31, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 95, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 97, myHeight + (d.height - myHeight)/2 - size_pixel * 30, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 97, myHeight + (d.height - myHeight)/2 - size_pixel * 29, size_pixel, size_pixel * 3);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 91, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 94, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 96, myHeight + (d.height - myHeight)/2 - size_pixel * 35, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 96, myHeight + (d.height - myHeight)/2 - size_pixel * 36, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 100, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 101, myHeight + (d.height - myHeight)/2 - size_pixel * 32, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 102, myHeight + (d.height - myHeight)/2 - size_pixel * 33, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 103, myHeight + (d.height - myHeight)/2 - size_pixel * 34, size_pixel * 2, size_pixel);



        // Горы
        g.setColor(new Color(55, 47, 71));
        g.fillRect((d.width - myWidth)/2, myHeight + (d.height - myHeight)/2 - size_pixel * 66, size_pixel * 68, size_pixel);
        g.fillRect((d.width - myWidth)/2, myHeight + (d.height - myHeight)/2 - size_pixel * 67, size_pixel * 31, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 4, myHeight + (d.height - myHeight)/2 - size_pixel * 68, size_pixel * 23, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 8, myHeight + (d.height - myHeight)/2 - size_pixel * 69, size_pixel * 13, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 14, myHeight + (d.height - myHeight)/2 - size_pixel * 70, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 37, myHeight + (d.height - myHeight)/2 - size_pixel * 67, size_pixel * 16, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 60, myHeight + (d.height - myHeight)/2 - size_pixel * 67, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 63, myHeight + (d.height - myHeight)/2 - size_pixel * 68, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 64, myHeight + (d.height - myHeight)/2 - size_pixel * 69, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 65, myHeight + (d.height - myHeight)/2 - size_pixel * 70, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 66, myHeight + (d.height - myHeight)/2 - size_pixel * 71, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 80, myHeight + (d.height - myHeight)/2 - size_pixel * 67, size_pixel * 71, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 80, myHeight + (d.height - myHeight)/2 - size_pixel * 68, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 80, myHeight + (d.height - myHeight)/2 - size_pixel * 69, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 87, myHeight + (d.height - myHeight)/2 - size_pixel * 68, size_pixel * 13, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 90, myHeight + (d.height - myHeight)/2 - size_pixel * 69, size_pixel * 7, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 108, myHeight + (d.height - myHeight)/2 - size_pixel * 68, size_pixel * 43, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 111, myHeight + (d.height - myHeight)/2 - size_pixel * 69, size_pixel * 40, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 112, myHeight + (d.height - myHeight)/2 - size_pixel * 70, size_pixel * 13, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 114, myHeight + (d.height - myHeight)/2 - size_pixel * 71, size_pixel * 10, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 116, myHeight + (d.height - myHeight)/2 - size_pixel * 72, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 119, myHeight + (d.height - myHeight)/2 - size_pixel * 73, size_pixel * 4, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 127, myHeight + (d.height - myHeight)/2 - size_pixel * 70, size_pixel * 24, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 129, myHeight + (d.height - myHeight)/2 - size_pixel * 71, size_pixel * 22, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 132, myHeight + (d.height - myHeight)/2 - size_pixel * 72, size_pixel * 18, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 134, myHeight + (d.height - myHeight)/2 - size_pixel * 73, size_pixel * 15, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 136, myHeight + (d.height - myHeight)/2 - size_pixel * 74, size_pixel * 11, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 138, myHeight + (d.height - myHeight)/2 - size_pixel * 75, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 139, myHeight + (d.height - myHeight)/2 - size_pixel * 76, size_pixel * 5, size_pixel);

        // Солнце
        g.setColor(new Color(250, 246, 208));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 12, myHeight + (d.height - myHeight)/2 - size_pixel * 91, size_pixel * 5, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 11, myHeight + (d.height - myHeight)/2 - size_pixel * 90, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 17, myHeight + (d.height - myHeight)/2 - size_pixel * 90, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 13, myHeight + (d.height - myHeight)/2 - size_pixel * 92, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 13, myHeight + (d.height - myHeight)/2 - size_pixel * 86, size_pixel * 3, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 14, myHeight + (d.height - myHeight)/2 - size_pixel * 62, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 13, myHeight + (d.height - myHeight)/2 - size_pixel * 61, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 11, myHeight + (d.height - myHeight)/2 - size_pixel * 60, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 13, myHeight + (d.height - myHeight)/2 - size_pixel * 59, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 11, myHeight + (d.height - myHeight)/2 - size_pixel * 58, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 14, myHeight + (d.height - myHeight)/2 - size_pixel * 57, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 13, myHeight + (d.height - myHeight)/2 - size_pixel * 56, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 15, myHeight + (d.height - myHeight)/2 - size_pixel * 56, size_pixel * 2, size_pixel);

        g.setColor(new Color(218, 201, 185));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 11, myHeight + (d.height - myHeight)/2 - size_pixel * 91, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 11, myHeight + (d.height - myHeight)/2 - size_pixel * 87, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 12, myHeight + (d.height - myHeight)/2 - size_pixel * 86, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 16, myHeight + (d.height - myHeight)/2 - size_pixel * 86, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 17, myHeight + (d.height - myHeight)/2 - size_pixel * 87, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 17, myHeight + (d.height - myHeight)/2 - size_pixel * 91, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 16, myHeight + (d.height - myHeight)/2 - size_pixel * 92, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 12, myHeight + (d.height - myHeight)/2 - size_pixel * 92, size_pixel, size_pixel);

        // Маяк
        g.setColor(new Color(243, 198, 179));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 67, myHeight + (d.height - myHeight)/2 - size_pixel * 65, size_pixel * 5, size_pixel * 12);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 68, myHeight + (d.height - myHeight)/2 - size_pixel * 78, size_pixel * 5, size_pixel * 13);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 94, size_pixel * 4, size_pixel * 16);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 100, size_pixel * 3, size_pixel * 6);

        g.setColor(new Color(117, 107, 134));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 100, size_pixel * 5, size_pixel * 6);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 94, size_pixel * 6, size_pixel * 16);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 78, size_pixel * 7, size_pixel * 13);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 65, size_pixel * 9, size_pixel * 13);

        // Дом: стена
        g.fillRect((d.width - myWidth)/2 + size_pixel * 94, myHeight + (d.height - myHeight)/2 - size_pixel * 52, size_pixel * 6, size_pixel * 5);

        // Маяк и стена дома
        g.setColor(new Color(171, 145, 158));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 87, myHeight + (d.height - myHeight)/2 - size_pixel * 52, size_pixel * 7, size_pixel * 5);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 88, myHeight + (d.height - myHeight)/2 - size_pixel * 53, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 89, myHeight + (d.height - myHeight)/2 - size_pixel * 55, size_pixel * 3, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 90, myHeight + (d.height - myHeight)/2 - size_pixel * 56, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 54, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 54, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 55, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 55, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 56, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 56, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 57, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 58, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 58, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 59, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 60, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 61, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 62, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 63, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 63, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 64, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 64, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 65, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 67, size_pixel * 3, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 68, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 69, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 70, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 71, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 72, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 73, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 74, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 75, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 76, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 78, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 79, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 80, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 81, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 82, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 83, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 84, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 85, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 87, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 88, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 89, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 90, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 93, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 95, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 98, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 99, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 74, myHeight + (d.height - myHeight)/2 - size_pixel * 99, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 100, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 100, size_pixel, size_pixel);


        // Дом: окна
        g.setColor(new Color(250, 246, 208));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 88, myHeight + (d.height - myHeight)/2 - size_pixel * 51, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 90, myHeight + (d.height - myHeight)/2 - size_pixel * 51, size_pixel, size_pixel);

        // Маяк
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 98, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 97, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 96, size_pixel, size_pixel);

        g.setColor(new Color(254, 255, 255));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 98, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 97, size_pixel, size_pixel);


        // Дом: крыша, окна
        g.setColor(new Color(55, 47, 71));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 90, myHeight + (d.height - myHeight)/2 - size_pixel * 57, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 91, myHeight + (d.height - myHeight)/2 - size_pixel * 56, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 92, myHeight + (d.height - myHeight)/2 - size_pixel * 55, size_pixel * 6, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 92, myHeight + (d.height - myHeight)/2 - size_pixel * 54, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 93, myHeight + (d.height - myHeight)/2 - size_pixel * 53, size_pixel * 7, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 90, myHeight + (d.height - myHeight)/2 - size_pixel * 54, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 92, myHeight + (d.height - myHeight)/2 - size_pixel * 51, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 95, myHeight + (d.height - myHeight)/2 - size_pixel * 51, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 97, myHeight + (d.height - myHeight)/2 - size_pixel * 51, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 87, myHeight + (d.height - myHeight)/2 - size_pixel * 53, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 88, myHeight + (d.height - myHeight)/2 - size_pixel * 54, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 89, myHeight + (d.height - myHeight)/2 - size_pixel * 56, size_pixel, size_pixel);

        // Маяк
        g.fillRect((d.width - myWidth)/2 + size_pixel * 74, myHeight + (d.height - myHeight)/2 - size_pixel * 98, size_pixel * 3, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 98, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 96, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 78, myHeight + (d.height - myHeight)/2 - size_pixel * 95, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 94, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 79, myHeight + (d.height - myHeight)/2 - size_pixel * 94, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 78, myHeight + (d.height - myHeight)/2 - size_pixel * 93, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 92, size_pixel * 7, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 92, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 93, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 75, myHeight + (d.height - myHeight)/2 - size_pixel * 93, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 101, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 102, size_pixel * 8, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 103, size_pixel * 7, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 104, size_pixel * 5, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 105, size_pixel * 4, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 74, myHeight + (d.height - myHeight)/2 - size_pixel * 106, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 74, myHeight + (d.height - myHeight)/2 - size_pixel * 107, size_pixel, size_pixel);

        g.setColor(new Color(76, 68, 92));
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 94, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 68, myHeight + (d.height - myHeight)/2 - size_pixel * 95, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 68, myHeight + (d.height - myHeight)/2 - size_pixel * 95, size_pixel, size_pixel * 4);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 93, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 92, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 91, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 103, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 104, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 71, myHeight + (d.height - myHeight)/2 - size_pixel * 105, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 72, myHeight + (d.height - myHeight)/2 - size_pixel * 106, size_pixel, size_pixel * 3);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 107, size_pixel, size_pixel * 2);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 84, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 70, myHeight + (d.height - myHeight)/2 - size_pixel * 85, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 76, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 77, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 67, size_pixel * 2, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 69, myHeight + (d.height - myHeight)/2 - size_pixel * 68, size_pixel, size_pixel);

        // Птицы
        g.fillRect((d.width - myWidth)/2 + size_pixel * 107, myHeight + (d.height - myHeight)/2 - size_pixel * 114, size_pixel, size_pixel * 2);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 107, myHeight + (d.height - myHeight)/2 - size_pixel * 114, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 109, myHeight + (d.height - myHeight)/2 - size_pixel * 115, size_pixel * 3, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 115, myHeight + (d.height - myHeight)/2 - size_pixel * 129, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 116, myHeight + (d.height - myHeight)/2 - size_pixel * 130, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 118, myHeight + (d.height - myHeight)/2 - size_pixel * 129, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 119, myHeight + (d.height - myHeight)/2 - size_pixel * 130, size_pixel * 2, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 127, myHeight + (d.height - myHeight)/2 - size_pixel * 133, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 129, myHeight + (d.height - myHeight)/2 - size_pixel * 132, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 131, myHeight + (d.height - myHeight)/2 - size_pixel * 133, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 132, myHeight + (d.height - myHeight)/2 - size_pixel * 132, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 106, myHeight + (d.height - myHeight)/2 - size_pixel * 133, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 107, myHeight + (d.height - myHeight)/2 - size_pixel * 134, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 109, myHeight + (d.height - myHeight)/2 - size_pixel * 135, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 111, myHeight + (d.height - myHeight)/2 - size_pixel * 134, size_pixel, size_pixel);

        g.fillRect((d.width - myWidth)/2 + size_pixel * 73, myHeight + (d.height - myHeight)/2 - size_pixel * 147, size_pixel * 3, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 76, myHeight + (d.height - myHeight)/2 - size_pixel * 146, size_pixel, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 77, myHeight + (d.height - myHeight)/2 - size_pixel * 147, size_pixel * 2, size_pixel);
        g.fillRect((d.width - myWidth)/2 + size_pixel * 78, myHeight + (d.height - myHeight)/2 - size_pixel * 146, size_pixel, size_pixel);


        setBackground(Color.black);
    }
    public static void main(String[] args) {
        LightHouse f = new LightHouse("Маяк");
        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent ev) {
                System.exit(0);
            }
        });
    }
}
