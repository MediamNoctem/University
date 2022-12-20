package calc.operation;
public class Subtractor
{
    private byte sub;
    public Subtractor(byte a) {
        this.sub=a;
    }
    public void sub(byte b) {
        this.sub-=b;
    }
    public byte getSub() {
        return this.sub;
    }
}