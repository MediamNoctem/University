package calc.operation;
public class Division
{
    private byte div;
    public Division(byte a) {
        this.div=a;
    }
    public void div(byte b) {
        div/=b;
    }
    public byte getDiv() {
        return div;
    }
}