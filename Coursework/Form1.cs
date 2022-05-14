using System;
using System.Collections;
using System.Drawing;
using System.Windows.Forms;
using System.Diagnostics;
using System.Numerics;
using System.IO;
using System.Drawing.Imaging;
using System.Text;

namespace Coursework
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            ComputeHash();
            //EllipticCurve.EllipticCurve p = new EllipticCurve.EllipticCurve();
        }
        private void ComputeHash()
        {
            Gost_34_11_2012 G = new Gost_34_11_2012(256);
            Gost_34_11_2012 G512 = new Gost_34_11_2012(512);
            byte[] message ={0x32,0x31};
            DigitalSignature ds = new DigitalSignature();
            BigInteger d = BigInteger.Parse("55441196065363246126355624130324183196576709222340016572108097750006097525544");
            string signature = ds.toFormDigitalSignature(message, d);
            
            textBox1.Text = signature;
        }
    }
    public class DigitalSignature
    {
        Gost_34_11_2012 G256 = new Gost_34_11_2012(256);
        BigInteger n = EllipticCurve.EllipticCurve.n;
        BigInteger e;
        
        public string toFormDigitalSignature(byte[] message, BigInteger signatureKey)
        {
            byte[] hash = G256.GetHash(message);
            BigInteger alpha = 0, k, r, s;
            Random rnd = new Random();
            EllipticCurve.EllipticCurvePoint C;
            EllipticCurve.EllipticCurvePoint G = new EllipticCurve.EllipticCurvePoint(EllipticCurve.EllipticCurve.x_G, EllipticCurve.EllipticCurve.y_G);

            for (int i = 0; i < hash.Length; i++)
                alpha += hash[i] * (BigInteger)(Math.Pow(2, i));

            e = alpha % n;
            if (e == 0) e = 1;

            while (true)
            {
                k = rnd.Next(0, n);
                if (k == 0) continue;

                C = G.scalMultNumByPointEC(k);
                r = C.x % n;
                if (r == 0) continue;
                s = (r * signatureKey + k * e) % n;
                if (s == 0) continue;
                break;
            }

            string digitalSignature, d;
            byte[] r_hash = r.ToByteArray();
            byte[] s_hash = s.ToByteArray();
            Array.Reverse(r_hash);
            Array.Reverse(s_hash);
            r_hash = G256.GetHash(r_hash);
            s_hash = G256.GetHash(s_hash);

            digitalSignature = BitConverter.ToString(r_hash) + "-" + BitConverter.ToString(s_hash);

            return digitalSignature;
        }
    }
    public static class RandomExtension
    {
        public static BigInteger Next(this Random random, BigInteger minValue, BigInteger maxValue)
        {
            int number_digits_min = minValue.ToString().Length, number_digits_max = maxValue.ToString().Length;
            int number_digits_in_num = random.Next(number_digits_min, number_digits_max);
            string num = "";
            int digit;

            for (int i = 0; i < number_digits_in_num; i++)
            {
                digit = random.Next(0, 10);
                num += digit.ToString();
            }
            return BigInteger.Parse(num);
        }
    }

    //public static class ConvertExtension
    //{
    //    public static string ToString(BigInteger value, int toBase)
    //    {

    //    }
    //}
}