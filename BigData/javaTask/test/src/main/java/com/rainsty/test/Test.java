package com.rainsty.test;

public class Test {
    public static void main(String[] args) {
        Student s = new Student();
        s.run();
        String sa = s.getName();
        Print.println(sa);
        s.eat();
        String sb = s.getSey();
        Print.println(sb);
        Print.println(s.getAge());
        // Print.println(Student.getAge()); 静态方法可以直接通过class.method调用
        // Print.println(Student.getWordYear());
        // Print.println(Students.getWordYear());

        Students ss = new Students(19);
        ss.eat();
        ss.run();
        Print.println(ss.getName());
        Print.println(ss.getSey());
        Print.println(ss.getAge());
        Print.println(ss.getWordYear());
    }
}
