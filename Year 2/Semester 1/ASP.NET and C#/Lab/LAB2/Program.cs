using System.Runtime.CompilerServices;

namespace LAB2
{
    class Program
    {
        void Palindrom(int n)
        {
            int x = 0;
            int y = n;
            while (y > 0)
            {
                x = x * 10 + y % 10;
                y /= 10;
            }
            if (x == n)
                Console.WriteLine($"The number {n} is a palindrome\n");
            else
                Console.WriteLine($"The number {n} is NOT a palindrome\n");
        }

        void Paritate()
        {
            int n = int.Parse(Console.ReadLine());
            int[] v = new int[n];
            if (n == 0) return;
            v[0] = int.Parse(Console.ReadLine());
            bool ok = true;
            for (int i = 1; i < n; ++i)
            {
                v[i] = int.Parse(Console.ReadLine());
                if ((v[i] & 1) == (v[i - 1] & 1))
                    ok = false;
            }
            if (ok) Console.WriteLine("Da");
            else Console.WriteLine("Nu");
        }
        static void Main(string[] args)
        {
            Employee emp = new Employee(1, "First", "Last", "4500");
            emp.Print();

            Program program = new Program();
            Console.WriteLine("Introduceti un numar: ");
            int n = int.Parse(Console.ReadLine());
            program.Palindrom(n);

            Console.WriteLine("Introduceti un numar n. Apoi introduceti n numere.");
            program.Paritate();
        }
    }
}
