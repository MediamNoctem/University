package calc.operation;
public class Multiplication
{
    private byte mult;
    public Multiplication() {
        mult=1;
    }
    public Multiplication(byte a) {
        this.mult=a;
    }
    public void mult(byte b) {
        mult*=b;
    }
    public byte getMult() {
        return mult;
    }
}