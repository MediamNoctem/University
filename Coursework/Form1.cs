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
        private DigitalSignature ds = new DigitalSignature();
        private byte[] imageOriginal;
        private BigInteger d;
        
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
                Stopwatch stopwatch = new Stopwatch();
                stopwatch.Start();

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
                        BigInteger signature = BigInteger.Parse(ds.ToFormDigitalSignature(image, d, beginningOfImage, height, width));

                        textBox2.Text = signature.ToString("X");
                        stopwatch.Stop();
                        label9.Text = "Время формирования подписи: " + ((float)(stopwatch.ElapsedMilliseconds / 1000.0f)).ToString() + " c";
                    }
                }
                else
                    MessageBox.Show("Формат пикселя не WRGB!");
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox2.Image = null;
            textBox3.Text = "";
            textBox6.Text = "";
            textBox4.Text = "";
            textBox5.Text = "";
            label10.Text = "";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            pictureBox1.Image = null;
            textBox1.Text = "";
            textBox2.Text = "";
            label9.Text = "";
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
                Stopwatch stopwatch = new Stopwatch();
                stopwatch.Start();

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
                        BigInteger sig = BigInteger.Parse(textBox4.Text, System.Globalization.NumberStyles.HexNumber);
                        string signature = sig.ToString();
                        bool res = ds.ToVerifyDigitalSignature(image, signature, Q, beginningOfImage, height, width);
                        textBox5.Text = res.ToString();
                        stopwatch.Stop();
                        label10.Text = "Время проверки подлинности: " + ((float)(stopwatch.ElapsedMilliseconds / 1000.0f)).ToString() + " c";
                    }
                }
            }
        }
    }
    public class DigitalSignature
    {
        Gost_34_11_2018 G256 = new Gost_34_11_2018(256);
        EllipticCurve.EllipticCurvePoint C;
        public EllipticCurve.EllipticCurvePoint G = new EllipticCurve.EllipticCurvePoint(EllipticCurve.EllipticCurve.x_G, EllipticCurve.EllipticCurve.y_G);
        BigInteger n = EllipticCurve.EllipticCurve.n;
        BigInteger e;

        private void Round(KeyPoint[] A, int n)
        {
            for (int i = 0; i < n; i++)
            {
                A[i].Pt.X = (float)Math.Round(A[i].Pt.X);
                A[i].Pt.Y = (float)Math.Round(A[i].Pt.Y);
            }
        }

        private KeyPoint[] Sort(KeyPoint[] A, int n, int angle, int heigth, int width)
        {
            float tmp;
            KeyPoint t;

            if (angle == 0)
            {
                for (int i = 0; i < n - 1; i++)
                {
                    for (int j = i + 1; j < n; j++)
                    {
                        if (A[i].Pt.Y > A[j].Pt.Y)
                        {
                            t = A[i];
                            A[i] = A[j];
                            A[j] = t;
                        }
                    }
                }

                for (int i = 0; i < n - 1; i++)
                {
                    for (int j = i + 1; j < n; j++)
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
                for (int i = 0; i < n; i++)
                {
                    if (!(A[k].Pt.X == A[i].Pt.X && A[k].Pt.Y == A[i].Pt.Y))
                    {
                        q.Enqueue(A[i].Pt.X);
                        q.Enqueue(A[i].Pt.Y);
                        k++;
                    }
                }
                KeyPoint[] B = new KeyPoint[q.Count / 2];
                for (int i = 0; i < B.Length; i++)
                {
                    B[i].Pt.X = q.Dequeue();
                    B[i].Pt.Y = q.Dequeue();
                }

                return B;
            }
            else
            {
                for (int i = 0; i < n; i++)
                {
                    tmp = A[i].Pt.Y;
                    A[i].Pt.Y = width - A[i].Pt.X - 1;
                    A[i].Pt.X = tmp;
                }
                A = Sort(A, n, 0, heigth, width);
                n = A.Length;

                for (int i = 0; i < n; i++)
                {

                    tmp = A[i].Pt.X;
                    A[i].Pt.X = heigth - A[i].Pt.Y - 1;
                    A[i].Pt.Y = tmp;
                }
                return A;
            }

        }

        private byte[] Reverse(byte[] ar, int n)
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
            return ar;
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
            Round(point, point.Length);
            point = Sort(point, point.Length, 0, height, width);

            byte[] pixel = new byte[point.Length * 4];
            int len = point.Length, h = 0;

            for (int i = 0; i < width; i++)
            {
                for (int j = 0; j < height; j++)
                {
                    if (h != len)
                    {
                        if (point[h].Pt.X == j && point[h].Pt.Y == i)
                        {
                            for (int q = 0; q < 4; q++)
                                pixel[h * 4 + q] = img[(j * width + i) * 4 + q + beginningOfImage];
                            h++;
                            if ((h != len) && (point[h].Pt.Y == point[h - 1].Pt.Y))
                                i--;
                        }
                    }
                    else
                        break;
                }
            }

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

            if ((!(r > 0 && r < n)) || (!(s > 0 && s < n)))
                return false;

            MemoryStream memoryStream = new MemoryStream();
            image.Save(memoryStream, ImageFormat.Bmp);
            byte[] img = memoryStream.ToArray();


            Bitmap message = new Bitmap(image);
            Mat imageOriginal = OpenCvSharp.Extensions.BitmapConverter.ToMat(message);
            point = ToFindReferencePoints(imageOriginal);
            Round(point, point.Length);
            List<byte> pixels = null;
            byte[] pixel = null;

            int len, h;
            bool flag = false;

            for (int i = 0; i < 2; i++)
            {
                if (!flag)
                {
                    pixels = new List<byte> { };

                    point = Sort(point, point.Length, i, height, width);
                    len = point.Length;
                    h = 0;

                    for (int t = 0; t < width; t++)
                    {
                        for (int l = 0; l < height; l++)
                        {
                            if (h != len)
                            {
                                if (point[h].Pt.X == l && point[h].Pt.Y == t)
                                {
                                    for (int q = 0; q < 4; q++)
                                        pixels.Add(img[(l * width + t) * 4 + q + beginningOfImage]);
                                    h++;
                                    if ((h != len) && (point[h].Pt.Y == point[h - 1].Pt.Y))
                                        t--;
                                }
                            }
                            else
                                break;
                        }
                    }
                    if (pixels.Count != (len * 4))
                    {
                        pixels = new List<byte> { };
                        h = 0;
                        for (int t = height - 1; t >= 0; t--)
                        {
                            for (int l = 0; l < width; l++)
                            {
                                if (h != len)
                                {
                                    if (point[h].Pt.X == t && point[h].Pt.Y == l)
                                    {
                                        for (int q = 0; q < 4; q++)
                                            pixels.Add(img[(t * width + l) * 4 + q + beginningOfImage]);
                                        h++;
                                        if ((h != len) && (point[h].Pt.X == point[h - 1].Pt.X) && (point[h].Pt.Y < point[h - 1].Pt.Y))
                                            t++;
                                    }
                                }
                                else
                                    break;
                            }
                        }
                    }

                    pixel = pixels.ToArray();
                }

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

                if (R == r)
                    return true;
                else
                {
                    if (flag != true)
                    {
                        pixel = Reverse(pixel, pixel.Length);
                        string st = "";
                        for (int t = 0; t < pixel.Length / 4; t++)
                        {
                            for (int q = 0; q < 4; q++)
                                st += pixel[t * 4 + q] + "  ";
                            st += "    ";
                        }
                        flag = true;
                        i--;
                    }
                    else
                        flag = false;
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