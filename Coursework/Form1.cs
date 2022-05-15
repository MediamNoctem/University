using System;
using System.Drawing;
using System.Windows.Forms;
using System.Diagnostics;
using System.Numerics;
using System.IO;
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
            BigInteger d = BigInteger.Parse("20");
            string signature = ds.toFormDigitalSignature(message, d);
            EllipticCurve.EllipticCurvePoint Q = ds.G.scalMultNumByPointEC(d);

            bool res = ds.toVerifyDigitalSignature(message, signature, Q);
            textBox1.Text = signature;
            textBox2.Text = res.ToString();
        }
    }
    public class DigitalSignature
    {
        Gost_34_11_2012 G256 = new Gost_34_11_2012(256);
        EllipticCurve.EllipticCurvePoint C;
        public EllipticCurve.EllipticCurvePoint G = new EllipticCurve.EllipticCurvePoint(EllipticCurve.EllipticCurve.x_G, EllipticCurve.EllipticCurve.y_G);
        BigInteger n = EllipticCurve.EllipticCurve.n;
        BigInteger e;

        public string toFormDigitalSignature(byte[] message, BigInteger signatureKey)
        {
            byte[] hash = G256.GetHash(message);
            BigInteger alpha = 0, k, r, s;
            Random rnd = new Random();

            for (int i = 0; i < hash.Length; i++)
                alpha += hash[i] * (BigInteger)(Math.Pow(2, i));

            e = alpha % n;
            if (e == 0) e = 1;

            while (true)
            {
                k = rnd.Next(0, n);
                if (k == 0 || k == n) continue;

                C = G.scalMultNumByPointEC(k);
                r = C.x % n;
                if (r == 0) continue;
                s = (r * signatureKey + k * e) % n;
                if (s == 0) continue;
                break;
            }
            string r_vector = r.ToBinaryString(256);
            string s_vector = s.ToBinaryString(256);

            return r_vector + s_vector;
        }

        BigInteger[] gcdex(BigInteger a, BigInteger b)
        {
            if (a == 0)
                return new BigInteger[] { b, 0, 1 };
            BigInteger[] gcd = gcdex(b % a, a);
            return new BigInteger[] { gcd[0], gcd[2] - (b / a) * gcd[1], gcd[1] };
        }
        BigInteger invmod(BigInteger a, BigInteger m)
        {
            BigInteger[] g = gcdex(a, m);
            if (g[0] > 1)
                return BigInteger.Zero;
            else
                return (g[1] % m + m) % m;
        }

        public bool toVerifyDigitalSignature(byte[] message, string digitalSignature, EllipticCurve.EllipticCurvePoint signatureVerificationKey)
        {
            BigInteger r = digitalSignature.Substring(0, 256).FromBinary();
            BigInteger s = digitalSignature.Substring(256).FromBinary();

            if ((!(r > 0 && r < n)) || (!(s > 0 && s < n)))
                return false;

            byte[] hash = G256.GetHash(message);
            BigInteger alpha = 0;

            for (int i = 0; i < hash.Length; i++)
                alpha += hash[i] * (BigInteger)Math.Pow(2, i);

            e = alpha % n;
            if (e == 0) e = 1;

            BigInteger v = invmod(e, n);
            BigInteger z1, z2;

            z1 = (s * v) % n;
            z2 = ((n - r) * v) % n;

            C = G.scalMultNumByPointEC(z1).addingPoint(signatureVerificationKey.scalMultNumByPointEC(z2));

            BigInteger R = C.x % n;

            if (R == r) 
                return true;
            else 
                return false;
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

    public static class BigIntegerExtension
    {
        public static string ToBinaryString(this BigInteger bigint, int maxNumOfDigits)
        {
            byte[] bytes = bigint.ToByteArray();
            int idx = bytes.Length - 1;

            StringBuilder base2 = new StringBuilder(bytes.Length * 8);
            string binary = Convert.ToString(bytes[idx], 2);

            base2.Append(binary);
            
            for (idx--; idx >= 0; idx--)
                base2.Append(Convert.ToString(bytes[idx], 2).PadLeft(8, '0'));
            
            int diff = maxNumOfDigits - base2.Length;

            string zero = "";

            for (int i = 0; i < diff; i++)
                zero += "0";

            if (diff < 0)
                base2.Remove(0, Math.Abs(diff));

            return zero + base2.ToString();
        }
    }

    public static class StringExtension
    {
        public static BigInteger FromBinary(this string input)
        {
            BigInteger big = new BigInteger();
            foreach (var c in input)
            {
                big <<= 1;
                big += c - '0';
            }

            return big;
        }
    }
}