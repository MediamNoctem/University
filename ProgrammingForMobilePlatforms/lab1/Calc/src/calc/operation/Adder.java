package calc.operation;
public class Adder
{
    private byte sum;
    public Adder() {
        sum=0;
    }
    public Adder(byte a) {
        this.sum=a;
    }
    public void add(byte b) {
        sum+=b;
    }
    public byte getSum() {
        return sum;
    }
}