package game;
import javax.swing.*;
import java.awt.*;
public class Ball extends JLabel {
    private String color;
//    private int height;
//    private int width;
//    private int radius;

    private String cell_color = "#666666";
    private String[] allColor = {"#9F7672", "#E3A49D", "#F7435E", "#D4C0BF", "#465153"};

    public String getColor() {
        return this.color;
    }

    public void setColor(int ind_color) {
        this.color = allColor[ind_color];
    }

//    public int getHeight() {
//        return this.height;
//    }
//
//    public void setHeight(int height) {
//        this.height = height;
//    }
//
//    public int getWidth() {
//        return this.width;
//    }
//
//    public void setWidth(int width) {
//        this.width = width;
//    }
//
//    public int getRadius() {
//        return this.radius;
//    }
//
//    public void setRadius(int radius) {
//        this.radius = radius;
//    }

//    , int height, int width, int radius
//    setHeight(height);
//    setWidth(width);
//    setRadius(radius);
    public Ball() {
//        setColor(ind_color);
        setBackground(Color.decode(this.cell_color));
        setForeground(Color.decode(this.cell_color));
        setOpaque(true);
        setText("0");
    }
}