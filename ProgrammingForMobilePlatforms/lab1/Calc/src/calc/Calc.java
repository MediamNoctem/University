package calc;
public class Calc {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        Calculator calc=new Calculator();
        System.out.println("2 + 2 = "+calc.sum((byte)2, (byte)2));
        System.out.println("4 - 1 = "+calc.sub((byte)4, (byte)1));
        System.out.println("3 * 5 = "+calc.mult((byte)3, (byte)5));
        System.out.println("15 / 3 = "+calc.div((byte)15, (byte)3));
        System.out.println("5 << 1 = "+calc.shift((byte)5, (byte)1));
    }
}