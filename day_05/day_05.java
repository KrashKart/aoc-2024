package day_05;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class day_05 {
    private static String filePath = "day_05/day_05.txt";
    private List<List<Integer>> rules;
    private List<List<Integer>> updates;

    public day_05() {
        rules = new ArrayList<>();
        updates = new ArrayList<>();
    }
    
    private List<Integer> toInt(String[] ses) {
        return List.of(ses).stream().map(x -> Integer.valueOf(x)).toList();
    }

    private void readFile() {
        try {
            String line;
            String[] parts;
            Scanner sc = new Scanner(new File(filePath));
            while (sc.hasNextLine()) {
              line = sc.nextLine();
              if (line.contains("|")) {
                parts = line.split("\\|");
                rules.add(toInt(parts));
              } else if (line.contains(",")) {
                parts = line.split(",");
                updates.add(toInt(parts));
              }
            }
            sc.close();
          } catch (FileNotFoundException e) {
            System.out.println("File not found!");
          }
    }

    private void solution() {
        int part1 = 0;
        int part2 = 0;
        List<Integer> updateSorted;

        for (List<Integer> update : updates) {
            updateSorted = new ArrayList<>(update);
            updateSorted.sort((x, y) -> {
                                for (List<Integer> r : this.rules) {
                                    if (r.equals(List.of(x, y))) return -1;
                                    else if (r.equals(List.of(y, x))) return 1;
                                    }
                                return 0;
                            });
            if (update.equals(updateSorted)) {
                part1 += update.get(update.size() / 2);
            } else {
                part2 += updateSorted.get(update.size() / 2);
            }
        }

        System.out.printf("Part 1: %d\nPart 2: %d\n", part1, part2);
    }

    public static void main(String[] args) {
        day_05 day05 = new day_05();
        day05.readFile();
        day05.solution();
    }
}