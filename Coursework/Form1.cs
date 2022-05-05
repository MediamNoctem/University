using System;
using System.Collections;
using System.Drawing;
using System.Windows.Forms;
using System.Diagnostics;
using System.Numerics;
using System.IO;
using System.Drawing.Imaging;

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
            byte[] res = G.GetHash(message);
            byte[] res2 = G512.GetHash(message);
            string h256 = BitConverter.ToString(res);
            string h512 = BitConverter.ToString(res2);
            MessageBox.Show(h256);
            MessageBox.Show(h512);
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

            byte[] r_hash = G256.GetHash(r);
            byte[] s_hash = G256.GetHash(s);

            string digitalSignature = (r_hash.ToString() + s_hash.ToString());
            
            return digitalSignature;
        }
    }
}
