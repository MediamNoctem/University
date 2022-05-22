using System;
using System.Drawing;
using System.Drawing.Imaging;
using System.Collections.Generic;
using System.Windows.Forms;
using System.Diagnostics;
using System.Numerics;
using System.IO;
using System.Text;
using OpenCvSharp;
using OpenCvSharp.XFeatures2D;

namespace Coursework
{
    public partial class Form1 : Form
    {
        private int height, width, beginningOfImage;
        DigitalSignature ds = new DigitalSignature();
        private byte[] imageOriginal;
        BigInteger d;
        
        public Form1()
        {
            InitializeComponent();
        }

        private string BeginningOfImage(byte b1, byte b2, byte b3, byte b4)
        {
            return Convert.ToString(b1, 16) + Convert.ToString(b2, 16) + Convert.ToString(b3, 16) + Convert.ToString(b4, 16);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "(*.bmp)|*.bmp";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                pictureBox1.Image = Image.FromFile(ofd.FileName);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
                MessageBox.Show("Выберите изображение!", "Ошибка!");
            else
            {
                Image image = pictureBox1.Image;
                height = image.Height;
                width = image.Width;

                MemoryStream memoryStream = new MemoryStream();
                image.Save(memoryStream, ImageFormat.Bmp);
                imageOriginal = memoryStream.ToArray();

                beginningOfImage = Convert.ToInt32(BeginningOfImage(imageOriginal[13], imageOriginal[12], imageOriginal[11], imageOriginal[10]), 16);

                if (imageOriginal[28] == 32)
                {
                    if (textBox1.Text == "")
                        MessageBox.Show("Введите ключ подписи!", "Ошибка!");
                    else
                    {
                        d = BigInteger.Parse(textBox1.Text);
                        string signature = ds.ToFormDigitalSignature(image, d, beginningOfImage, height, width);
                        EllipticCurve.EllipticCurvePoint Q = ds.G.scalMultNumByPointEC(d);

                        StreamWriter sw = new StreamWriter("file.txt");
                        sw.WriteLine(Q.x);
                        sw.WriteLine(Q.y);
                        sw.Close();

                        textBox2.Text = signature;
                    }
                }
                else
                    MessageBox.Show("Формат пикселя не WRGB!");
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "(*.bmp)|*.bmp";

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                pictureBox2.Image = Image.FromFile(ofd.FileName);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (pictureBox2.Image == null)
                MessageBox.Show("Выберите изображение!", "Ошибка!");
            else
            {
                Image image = pictureBox2.Image;
                height = image.Height;
                width = image.Width;

                MemoryStream memoryStream = new MemoryStream();
                image.Save(memoryStream, ImageFormat.Bmp);
                imageOriginal = memoryStream.ToArray();

                if (textBox3.Text == "" || textBox6.Text == "")
                    MessageBox.Show("Введите ключ проверки подписи!", "Ошибка!");
                else
                {
                    if (textBox4.Text == "")
                        MessageBox.Show("Введите ЭЦП!", "Ошибка!");
                    else
                    {
                        beginningOfImage = Convert.ToInt32(BeginningOfImage(imageOriginal[13], imageOriginal[12], imageOriginal[11], imageOriginal[10]), 16);

                        EllipticCurve.EllipticCurvePoint Q = new EllipticCurve.EllipticCurvePoint(BigInteger.Parse(textBox3.Text), BigInteger.Parse(textBox6.Text));
                        string signature = textBox4.Text;
                        bool res = ds.ToVerifyDigitalSignature(image, signature, Q, beginningOfImage, height, width);
                        textBox5.Text = res.ToString();
                    }
                }
            }
        }
    }
    public class DigitalSignature
    {
        Gost_34_11_2012 G256 = new Gost_34_11_2012(256);
        EllipticCurve.EllipticCurvePoint C;
        public EllipticCurve.EllipticCurvePoint G = new EllipticCurve.EllipticCurvePoint(EllipticCurve.EllipticCurve.x_G, EllipticCurve.EllipticCurve.y_G);
        BigInteger n = EllipticCurve.EllipticCurve.n;
        BigInteger e;

        //private byte[] Rotate90(byte[] ar, int beginningOfImage, int height, int width)
        //{
        //    byte[] res = new byte[ar.LongLength];
        //    for (int i = 0; i < height; i++)
        //        for (int j = 0; j < width; j++)
        //            res[i * height + j] = ar[]
        //}

        private KeyPoint[] Sort(KeyPoint[] A, int n, string angle, int heigth, int width)
        {
            int i, j;
            float tmp;
            KeyPoint t;

            for (i = 0; i < n; i++)
            {
                A[i].Pt.X = (float)Math.Round(A[i].Pt.X);
                A[i].Pt.Y = (float)Math.Round(A[i].Pt.Y);
            }
            if (angle == "0")
            {
                for (i = 0; i < n - 1; i++)
                {
                    for (j = i + 1; j < n; j++)
                    {
                        if (A[i].Pt.Y > A[j].Pt.Y)
                        {
                            t = A[i];
                            A[i] = A[j];
                            A[j] = t;
                        }
                    }
                }

                for (i = 0; i < n - 1; i++)
                {
                    for (j = i + 1; j < n; j++)
                    {
                        if (A[i].Pt.Y == A[j].Pt.Y)
                        {
                            if (A[i].Pt.X > A[j].Pt.X)
                            {
                                t = A[i];
                                A[i] = A[j];
                                A[j] = t;
                            }
                        }
                    }
                }
                    
                Queue<float> q = new Queue<float>();
                q.Enqueue(A[0].Pt.X);
                q.Enqueue(A[0].Pt.Y);
                int k = 0;
                for (i = 0; i < n; i++)
                {
                    if (!(A[k].Pt.X == A[i].Pt.X && A[k].Pt.Y == A[i].Pt.Y))
                    {
                        q.Enqueue(A[i].Pt.X);
                        q.Enqueue(A[i].Pt.Y);
                        k++;
                    }
                }
                KeyPoint[] B = new KeyPoint[q.Count / 2];
                for (i = 0; i < B.Length; i++)
                {
                    B[i].Pt.X = q.Dequeue();
                    B[i].Pt.Y = q.Dequeue();
                }

                return B;
            }
            else
            {
                if (angle == "90")
                {
                    for (i = 0; i < n; i++)
                    {
                        tmp = A[i].Pt.Y;
                        A[i].Pt.Y = width - A[i].Pt.X - 1;
                        A[i].Pt.X = tmp;
                    }

                    A = Sort(A, n, "0", heigth, width);
                    n = A.Length;

                    for (i = 0; i < n; i++)
                    {
                        tmp = A[i].Pt.X;
                        A[i].Pt.X = width - A[i].Pt.Y - 1;
                        A[i].Pt.Y = tmp;
                    }
                    return A;
                }
                else
                {
                    if (angle == "180")
                    {
                        for (i = 0; i < n; i++)
                        {
                            A[i].Pt.X = width - A[i].Pt.X - 1;
                            A[i].Pt.Y = heigth - A[i].Pt.Y - 1;
                        }

                        A = Sort(A, n, "0", heigth, width);
                        n = A.Length;

                        for (i = 0; i < n; i++)
                        {
                            A[i].Pt.X = width - A[i].Pt.X - 1;
                            A[i].Pt.Y = heigth - A[i].Pt.Y - 1;
                        }
                        return A;
                    }
                    else
                    {
                        return null;
                    }
                }
            }
            
        }

        private void Reverse(byte[] ar, int n)
        {
            byte tmp;
            int len;

            if (n % 2 != 0)
                len = (n - 4) / 8;
            else
                len = n / 8;

            for (int i = 0; i < len; i++)
                for (int q = 0; q < 4; q++)
                {
                    tmp = ar[i * 4 + q];
                    ar[i * 4 + q] = ar[n - i * 4 - (4 - q)];
                    ar[n - i * 4 - (4 - q)] = tmp;
                }
        }

        private KeyPoint[] ToFindReferencePoints(InputArray image)
        {
            SURF surf = SURF.Create(1500);
            KeyPoint[] point = surf.Detect(image);

            return point;
        }

        public string ToFormDigitalSignature(Image image, BigInteger signatureKey, int beginningOfImage, int height, int width)
        {
            MemoryStream memoryStream = new MemoryStream();
            image.Save(memoryStream, ImageFormat.Bmp);
            byte[] img = memoryStream.ToArray();

            Bitmap message = new Bitmap(image);
            Mat imageOriginal = OpenCvSharp.Extensions.BitmapConverter.ToMat(message);

            KeyPoint[] point = ToFindReferencePoints(imageOriginal);

            point = Sort(point, point.Length, "0", height, width);
            MessageBox.Show("len = " + point.Length.ToString());

            byte[] pixel = new byte[point.Length * 4];
            int len = point.Length, h = 0;

            // 00101001000101110110111010110011010100101110100110010011011000100000011100000000100011101011010111000011011100100101010011000001000000100001000000101010110111010111000001101101011101010010100100110001110011110111101111000110110000011000100111101010111110001001101011101010010100110000000100111101000111111100000111010100010001100000010110010011000110011010001001110111010011111000101101011001111100101100111110111111101101001111110111110011011000000011001011100101101011000001000001000010000100001101110000010110
            // 72488970228380509287422715226575535698893157273063074627791787432852706183111
            // 62070622898698443831883535403436258712770888294397026493185421712108624767191
            
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    if ((h / 4) != len)
                    {
                        if (point[h / 4].Pt.X == j && point[h / 4].Pt.Y == i)
                        {
                            for (int q = 0; q < 4; q++)
                            {
                                pixel[h + q] = img[(i * width + j) * 4 + q + beginningOfImage];
                            }
                            h += 4;
                        }
                    }
                    else
                        break;
                }
            }

            string sr = "", sep;
            len = pixel.Length;
            for (int i = 0; i < len; i += 4)
            {
                if (i % 3 == 1)
                    sep = "\n";
                else
                    sep = "        ";
                sr += pixel[i].ToString() + " " + pixel[i + 1].ToString() + " " + pixel[i + 2].ToString() + " " + pixel[i + 3].ToString() + sep;
            }
            MessageBox.Show(sr);

            StreamWriter sw = new StreamWriter("file1.txt");
            for (int i = 0; i < point.Length; i++)
                sw.WriteLine(point[i].Pt.X.ToString() + " " + point[i].Pt.Y.ToString());
            sw.Close();


            byte[] hash = G256.GetHash(pixel);
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

        public bool ToVerifyDigitalSignature(Image image, string digitalSignature, EllipticCurve.EllipticCurvePoint signatureVerificationKey, int beginningOfImage, int height, int width)
        {
            BigInteger r = digitalSignature.Substring(0, 256).FromBinary();
            BigInteger s = digitalSignature.Substring(256).FromBinary();
            KeyPoint[] point;
            string[] angle = { "0", "90", "180" };
            byte[] pixel = null;

            if ((!(r > 0 && r < n)) || (!(s > 0 && s < n)))
                return false;

            MemoryStream memoryStream = new MemoryStream();
            image.Save(memoryStream, ImageFormat.Bmp);
            byte[] img = memoryStream.ToArray();


            Bitmap message = new Bitmap(image);
            Mat imageOriginal = OpenCvSharp.Extensions.BitmapConverter.ToMat(message);
            point = ToFindReferencePoints(imageOriginal);

            int len, h = 0, flag = 0;

            for (int i = 0; i < angle.Length; i++)
            {
                MessageBox.Show("i = " + i.ToString() + "\nflag = " + flag.ToString());

                if (flag != 1)
                {
                    point = Sort(point, point.Length, angle[i], height, width);
                    len = point.Length;
                    pixel = new byte[len * 4];

                    for (int t = 0; t < height; t++)
                    {
                        for (int l = 0; l < width; l++)
                        {
                            if (h / 4 != len)
                            {
                                if (point[h / 4].Pt.X == l && point[h / 4].Pt.Y == t)
                                {
                                    for (int q = 0; q < 4; q++)
                                        pixel[h + q] = img[(t * width + l) * 4 + q + beginningOfImage];
                                    h += 4;
                                }
                            }
                            else
                                break;
                        }
                    }
                }

                string sr = "", sep;
                len = pixel.Length;
                for (int t = 0; t < len; t += 4)
                {
                    if (t % 3 == 1)
                        sep = "\n";
                    else
                        sep = "        ";
                    sr += pixel[t].ToString() + " " + pixel[t + 1].ToString() + " " + pixel[t + 2].ToString() + " " + pixel[t + 3].ToString() + sep;
                }
                MessageBox.Show(sr);



                byte[] hash = G256.GetHash(pixel);
                BigInteger alpha = 0;

                for (int k = 0; k < hash.Length; k++)
                    alpha += hash[k] * (BigInteger)Math.Pow(2, k);

                e = alpha % n;
                if (e == 0) e = 1;

                BigInteger v = invmod(e, n);
                BigInteger z1, z2;

                z1 = (s * v) % n;
                z2 = ((n - r) * v) % n;

                C = G.scalMultNumByPointEC(z1).addingPoint(signatureVerificationKey.scalMultNumByPointEC(z2));

                BigInteger R = C.x % n;

                StreamWriter sw = new StreamWriter("file.txt");
                for (int k = 0; k < point.Length; k++)
                    sw.WriteLine(point[k].Pt.X.ToString() + " " + point[k].Pt.Y.ToString());
                sw.Close();
                MessageBox.Show("Файл!");

                if (R == r)
                    return true;
                else
                {
                    if (angle[i] == "180")
                    {
                        if (flag != 1)
                        {
                            Reverse(pixel, pixel.Length);
                            string st = "";
                            for (int t = 0; t < pixel.Length / 4; t++)
                            {
                                for (int q = 0; q < 4; q++)
                                    st += pixel[t * 4 + q] + "  ";
                                st += "    ";
                            }
                            MessageBox.Show("Reverse:\n" + st);
                            flag = 1;
                            i--;
                        }
                        else
                            i++;
                    }
                }
            }
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