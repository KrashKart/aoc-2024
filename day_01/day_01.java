package day_01;

import java.util.HashMap;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class day_01 {
    private static String filePath = "day_01/day_01.txt";
    private PriorityQueue<Integer> a;
    private PriorityQueue<Integer> b;
    private HashSet<Integer> s; // used for a in part 2
    private HashMap<Integer, Integer> h; // used to count instances in b in part 2

    public day_01() {
        this.a = new PriorityQueue<>();
        this.b = new PriorityQueue<>();
        this.s = new HashSet<>();
        this.h = new HashMap<>();
    }

    private void readFile() {
        try {
            Scanner sc = new Scanner(new File(filePath));
            while (sc.hasNextLine()) {
              String[] line = sc.nextLine().split("\s{3}");
              int i = Integer.valueOf(line[0]);
              int j = Integer.valueOf(line[1]);
              a.add(i);
              b.add(j);

              s.add(i);
              h.put(j, h.getOrDefault(j, 0) + 1);
            }
            sc.close();
          } catch (FileNotFoundException e) {
            System.out.println("File not found!");
            e.printStackTrace();
          }
    }

    private void part1() {
        int total = 0;
        while (!this.a.isEmpty()) {
            total += Math.abs(a.poll() - b.poll());
        }
        System.out.println(String.format("Part 1: %s", total));
    }

    private void part2() {
        int total = 0;
        for (Integer i : this.s) {
            total += i * h.getOrDefault(i, 0);
        }
        System.out.println(String.format("Part 2: %s", total));
    }

    public static void main(String[] args) {
        day_01 d = new day_01();
        d.readFile();
        d.part1();
        d.part2();
    }
}