import java.util.Arrays;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        ex1();
        ex2();
    }

    public static void ex1() {
        // a)
        Scanner scanner = new Scanner(System.in);
        int n;
        do {
            n = scanner.nextInt();
        } while (n < 0 || n > 5);

        // b)
        int[] t = new int[n];
        for (int i = 0; i < n; ++i) {
            t[i] = scanner.nextInt();
        }
        System.out.println(Arrays.toString(t));

        // c)
        int i = 0;
        int j = t.length - 1;
        while (i < j) {
            t[i] ^= t[j]; t[j] ^= t[i]; t[i] ^= t[j];
            ++i;
            --j;
        }
        System.out.println(Arrays.toString(t));
    }

    public static void ex2() {
        // a)
        int[] t1 = {3, 1, 4, 0, 15, 20, 13, 9, 61};
        int[] t2 = {-10, 100, -50, 50, 14, -28, 38, 64};

        // b)
        shellSort(t1);
        shellSort(t2);
        System.out.println(Arrays.toString(t1));
        System.out.println(Arrays.toString(t2));

        // c)
        int n1 = t1.length;
        int n2 = t2.length;
        int[] t3 = new int[n1 + n2];
        int i = 0, j = 0, k = 0;
        while (i < n1 && j < n2) {
            if (t1[i] <= t2[j]) {
                t3[k] = t1[i];
                ++i; ++k;
            }
            else {
                t3[k] = t2[j];
                ++j; ++k;
            }
        }
        while (i < n1) {
            t3[k] = t1[i];
            ++i; ++k;
        }
        while (j < n2) {
            t3[k] = t2[j];
            ++j; ++k;
        }
        System.out.println(Arrays.toString(t3));
    }

    public static void shellSort(int[] t) {
        int n = t.length;
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; ++i) {
                int temp = t[i];
                int j;
                for (j = i; j >= gap && temp < t[j - gap]; j -= gap) {
                    t[j] = t[j - gap];
                }
                t[j] = temp;
            }
        }
    }
}