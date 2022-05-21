using System;
using System.Drawing;
using System.Drawing.Imaging;
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

            pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;

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

            pictureBox2.SizeMode = PictureBoxSizeMode.StretchImage;

            if (ofd.ShowDialog() == DialogResult.OK)
            {
                pictureBox2.Image = Image.FromFile(ofd.FileName);
                //var chartBackImage = new Bitmap(1, 1); //some bmp
                //chart1.Images.Add(new NamedImage("Image", chartBackImage));
                //chart1.ChartAreas[0].BackImage = ofd.FileName.ToString();
                //chart1.ChartAreas[0].BackImageWrapMode = ChartImageWrapMode.Scaled;
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
                        KeyPoint[] point = null;
                        bool res = ds.ToVerifyDigitalSignature(image, signature, Q, ref point, beginningOfImage, height, width);
                        textBox2.Text = signature;
                        textBox5.Text = res.ToString();


                        //Series s = chart1.Series[0];
                        //DataPoint dp = s.Points[0];
                        //ChartArea ca = chart1.ChartAreas[0];

                        //chart1.Series[0].Points.Clear();

                        //for (int i = 0; i < point.Length; i++)
                        //{
                        //    chart1.Series[0].Points.AddXY(point[i].Pt.X, Math.Sqrt((Math.Pow(10, 2) - Math.Pow(point[i].Pt.Y, 2))));
                        //    chart1.Series[0].Points.AddXY(point[i].Pt.X, -Math.Sqrt((Math.Pow(10, 2) - Math.Pow(point[i].Pt.Y, 2))));
                        //}
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

        // string XY, string UD, int heigth, int width
        private void Sort(KeyPoint[] A, int n, string XY, string UD, int heigth, int width)
        {
            int i, j;
            KeyPoint t;

            for (i = 0; i < n; i++)
            {
                A[i].Pt.X = (float)Math.Round(A[i].Pt.X);
                A[i].Pt.Y = (float)Math.Round(A[i].Pt.Y);
            }

            //MessageBox.Show(XY + "   " + UD);

            if (XY == "Y")
            {
                if (UD == "U")
                {
                    for (i = 0; i < n; i++)
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
                }
                else
                {
                    if (UD == "D")
                    {
                        for (i = 0; i < n; i++)
                        {
                            A[i].Pt.X = width - A[i].Pt.X - 1;
                            A[i].Pt.Y = heigth - A[i].Pt.Y - 1;
                        }
                        Sort(A, n, "Y", "U", heigth, width);

                        for (i = 0; i < n; i++)
                        {
                            A[i].Pt.X = width - A[i].Pt.X - 1;
                            A[i].Pt.Y = heigth - A[i].Pt.Y - 1;
                        }
                    }
                }
            }
            else
            {
                if (XY == "X")
                    if (UD == "U")
                    {

                    }
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

            // "Y", "U", height, width
            Sort(point, point.Length, "Y", "U", height, width);


            StreamWriter sw = new StreamWriter("file1.txt");
            for (int l = 0; l < point.Length; l++)
                sw.WriteLine(point[l].Pt.X.ToString() + " " + point[l].Pt.Y.ToString());
            sw.Close();



            byte[] pixel = new byte[point.Length * 4];
            int len = point.Length, h = 0;

            //MessageBox.Show("points = " + point.Length.ToString());

            // 00101001000101110110111010110011010100101110100110010011011000100000011100000000100011101011010111000011011100100101010011000001000000100001000000101010110111010111000001101101011101010010100100110001110011110111101111000110110000011000100111101010111110001001101011101010010100110000000100111101000111111100000111010100010001100000010110010011000110011010001001110111010011111000101101011001111100101100111110111111101101001111110111110011011000000011001011100101101011000001000001000010000100001101110000010110
            // 72488970228380509287422715226575535698893157273063074627791787432852706183111
            // 62070622898698443831883535403436258712770888294397026493185421712108624767191


            ////////////////////
            //////// Исправить!
            ////////////////////
            for (int i = 0; i < height; i++)
            {
                for (int j = 0; j < width; j++)
                {
                    if (h / 4 != len)
                    {
                        if (point[h / 4].Pt.X == j && point[h / 4].Pt.Y == i)
                        {
                            for (int q = 0; q < 4; q++)
                            {
                                pixel[h + q] = img[(i * height + j) * 4 + q + beginningOfImage];
                            }
                            h += 4;
                        }
                    }
                    else
                        break;
                }
            }

            //MessageBox.Show("pixels = " + (pixel.Length / 4).ToString());

            string sr = "", sep;
            len = pixel.Length;
            for (int i = 0; i < len; i += 4)
            {
                //MessageBox.Show((i + 1).ToString());
                if (i % 3 == 1)
                    sep = "\n";
                else 
                    sep = "        ";

                sr += pixel[i].ToString() + " " + pixel[i + 1].ToString() + " " + pixel[i + 2].ToString() + " " + pixel[i + 3].ToString() + sep;
                //sr += pixel[(len / 4) - i].ToString() + " " + pixel[(len / 4) - i + 1].ToString() + " " + pixel[(len / 4) - i + 2].ToString() + " " + pixel[(len / 4) - i + 3].ToString() + "         ";
                //sr += pixel[(len / 2) - i].ToString() + " " + pixel[(len / 2) - i + 1].ToString() + " " + pixel[(len / 2) - i + 2].ToString() + " " + pixel[(len / 2) - i + 3].ToString() + "         ";
                //sr += pixel[(3 * len / 4) - i].ToString() + " " + pixel[(3 * len / 4) - i + 1].ToString() + " " + pixel[(3 * len / 4) - i + 2].ToString() + " " + pixel[(3 * len / 4) - i + 3].ToString() + "\n";
            }

            MessageBox.Show(sr);

            MemoryStream memoryStream1 = new MemoryStream();
            image.Save(memoryStream1, ImageFormat.Bmp);

            byte[] im = memoryStream1.ToArray();
            byte[] hash = G256.GetHash(im);

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

        public bool ToVerifyDigitalSignature(Image image, string digitalSignature, EllipticCurve.EllipticCurvePoint signatureVerificationKey, ref KeyPoint[] point, int beginningOfImage, int height, int width)
        {
            BigInteger r = digitalSignature.Substring(0, 256).FromBinary();
            BigInteger s = digitalSignature.Substring(256).FromBinary();
            string[] XY = { "Y", "X" };
            string[] UD = { "U", "D" };

            if ((!(r > 0 && r < n)) || (!(s > 0 && s < n)))
                return false;

            Bitmap message = new Bitmap(image);
            Mat imageOriginal = OpenCvSharp.Extensions.BitmapConverter.ToMat(message);
            point = ToFindReferencePoints(imageOriginal);


            MemoryStream memoryStream = new MemoryStream();
            image.Save(memoryStream, ImageFormat.Bmp);
            byte[] img = memoryStream.ToArray();


            byte[] pixel = new byte[point.Length * 4];
            int len = point.Length, h = 0;

            for (int i = 0; i < XY.Length; i++)
            {
                for (int j = 0; j < UD.Length; j++)
                {
                    //XY[i], UD[j], height, width

                    Sort(point, point.Length, XY[i], UD[j], height, width);


                    for (int t = 0; t < height; t++)
                    {
                        for (int l = 0; l < width; l++)
                        {
                            if (h / 4 != len)
                            {
                                if (point[h / 4].Pt.X == l && point[h / 4].Pt.Y == t)
                                {
                                    for (int q = 0; q < 4; q++)
                                    {
                                        //MessageBox.Show((i * height + j + q + beginningOfImage).ToString() + ":   " + img[i * height + j + q + beginningOfImage].ToString());
                                        pixel[h + q] = img[i * height + j + q + beginningOfImage];
                                    }
                                    h += 4;
                                }
                            }
                            else
                                break;
                        }
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

                    StreamWriter sw = new StreamWriter("file.txt");
                    for (int k = 0; k < point.Length; k++)
                        sw.WriteLine(point[k].Pt.X.ToString() + " " + point[k].Pt.Y.ToString());
                    sw.Close();

                    //MessageBox.Show("Посмотри файл!");
                    //MessageBox.Show((R == r).ToString());

                    if (R == r)
                        return true;
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