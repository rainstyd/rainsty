package com.rainsty.test;

class Student implements Persion, People {
    public void run() {
        Print.println("running...");
    }

    public String getName() {
        return "aaa";
    }

    public void eat() {
        Print.println("eating...");
    }

    public String getSey() {
        return "bbb";
    }

    final int getAge() {
        return 10;
    }

    public int getWordYear() {
        return 11;
    }
}

class Students extends Student {
    public int wordyear;
    @Override
    public void run() {
        Print.println("is students running...");
    }

    // @Override
    // final int getAge() {
    //     return 20;
    // }

    public Students(int wordyear) {
        this.wordyear = wordyear;
    }

    @Override
    public int getWordYear() {
        return this.wordyear;
    }
}
