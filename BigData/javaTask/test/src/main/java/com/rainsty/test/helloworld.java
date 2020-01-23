package com.rainsty.test;

import java.util.Arrays;

public class helloworld {
    
    public static void main(String[] args) {
        
        System.out.println("Hello, world");
        int x = 1;
        System.out.println(x);
        Print.println(x);
        int y = 5;
        int z = y / 2;
        System.out.println(z);
        String a = "a";
        String b = "b";
        String c = a + b;
        System.out.println(c);
        Print.println(c);
        double d = 1.0 / 10;
        double e = 1 - 9.0 / 10;
        System.out.printf("%.2f, %.3f\n", d, e);
        char f = 'a';
        char g = '郭';
        System.out.println(f);
        System.out.println(g);
        char[] ch = new char[5];
        ch[0] = 'a';
        ch[1] = 'a';
        ch[2] = 'a';
        ch[3] = 'b';
        ch[4] = 'a';
        System.out.println(ch);
        System.out.println(ch.length);
        double s = (double) x;
        Print.println(s);
        
        Print.printf("%s\n", ch.length);
        Print.printf("%s\n", s);
        if (x == 0) {
            Print.printf("%s0\n", x);
        } else if (x == 1) {
            Print.printf("%s1\n", x);
        } else {
            Print.printf("%s2\n", x);
        }

        switch (x) {
            case 1:
                System.out.println("Selected 1");
                break;
            case 2:
                System.out.println("Selected 2");
                break;
            case 3:
                System.out.println("Selected 3");
                break;
        }

        while (x < 10) {
            x++;
            Print.println(x);
        }

        do {
            x--;
            Print.println(x);
        } while (x > 1);

        for (int i = -2; i <= x; i++) {
            Print.println(i);
            if (i < 0) {
                continue;
            } else {
                break;
            }
        }

        for (int i = 0; i < ch.length; i++) {
            char ci = ch[i];
            System.out.println(ci);

        }

        int[] ns = { 28, 12, 89, 73, 65, 18, 96, 50, 8, 36 };

        for (int i = 0; i < ns.length -1; i++) {
            for (int j = 0; j < ns.length - i - 1; j++) {
                if (ns[j] > ns[j+1]) {
                    int tmp = ns[j];
                    ns[j] = ns[j+1];
                    ns[j+1] = tmp;
                }
            }
        }

        System.out.println(Arrays.toString(ns));
        Print.println(Arrays.toString(ns));

        int[][] ns1 = {
            { 1, 2, 3, 4 },
            { 5, 6, 7, 8 },
            { 9, 10, 11, 12 }
        };
        System.out.println(ns1.length);
        Print.println(ns1.length);

        for (int[] arr : ns1) {
            for (int n : arr) {
                Print.println(n);
            }
        }
    }
}
