package calc;
import calc.operation.Adder;
import calc.operation.Subtractor;
import calc.operation.Multiplication;
import calc.operation.Division;
import calc.operation.Shift;
public class Calculator
{
    public byte sum(byte... a) {
        Adder adder=new Adder();
        for(byte i: a)
        {
            adder.add(i);
        }
        return adder.getSum();
    }
    public byte sub(byte... a) {
        Subtractor subtractor=new Subtractor(a[0]);
        for(byte i=1; i < a.length; i++)
        {

            subtractor.sub(a[i]);
        }
        return subtractor.getSub();
    }
    public byte mult(byte... a) {
        Multiplication mult=new Multiplication();
        for(byte i: a)
        {
            mult.mult(i);
        }
        return mult.getMult();
    }
    public byte div(byte... a) {
        Division division=new Division(a[0]);
        for(byte i=1; i < a.length; i++)
        {
            division.div(a[i]);
        }
        return division.getDiv();
    }
    public byte shift(byte... a) {
        Shift shift=new Shift(a[0]);
        for(int i=1; i < a.length; i++)
        {
            shift.shift(a[i]);
        }
        return shift.getShift();
    }
}