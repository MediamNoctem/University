package calc.operation;
public class Shift
{
    private byte sh;
    public Shift(byte a) {
        this.sh=a;
    }
    public void shift(byte b) {
        sh<<=b;
    }
    public byte getShift() {
        return sh;
    }
}