import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Day4java {
    static int part1() {
        ArrayList<String> data = new ArrayList<>();

        // Java IO ¯\_(ツ)_/¯
        File myObj = new File("input.txt");
        try (Scanner myReader = new Scanner(myObj)) {
            while (myReader.hasNextLine()) {
                data.add(myReader.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        
        int rows = data.size();
        int cols = data.get(0).length();

        char[] xmasBuf = {'X','M','A','S'};
        char[] samxBuf = {'S','A','M','X'};

        int result = 0;

        for (int y = 0; y < rows; y++) {
            for (int x = 0; x < cols; x++) {
                ArrayList<char[]> bufs = new ArrayList<>();

                if (y < rows - 3) {
                    bufs.add(new char[]{ data.get(y).charAt(x), data.get(y+1).charAt(x), data.get(y+2).charAt(x), data.get(y+3).charAt(x) });
                }
                if (x < cols - 3) {
                    bufs.add(new char[]{ data.get(y).charAt(x), data.get(y).charAt(x+1), data.get(y).charAt(x+2), data.get(y).charAt(x+3) });
                }
                if (y < rows - 3 && x < cols - 3) {
                    bufs.add(new char[]{ data.get(y).charAt(x), data.get(y+1).charAt(x+1), data.get(y+2).charAt(x+2), data.get(y+3).charAt(x+3) });
                }
                if (y >= 3 && x < cols - 3) {
                    bufs.add(new char[]{ data.get(y).charAt(x), data.get(y-1).charAt(x+1), data.get(y-2).charAt(x+2), data.get(y-3).charAt(x+3) });
                }
                for (char[] buf : bufs) {
                    if (Arrays.equals(buf, xmasBuf) || Arrays.equals(buf, samxBuf)) {
                        result += 1;
                    }
                }
            }
        }
        
        return result;
    }

    static int part2() {
        ArrayList<String> data = new ArrayList<>();

        // Java IO ¯\_(ツ)_/¯
        File myObj = new File("input.txt");
        try (Scanner myReader = new Scanner(myObj)) {
            while (myReader.hasNextLine()) {
                data.add(myReader.nextLine());
            }
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

        int rows = data.size();
        int cols = data.get(0).length();

        int result = 0;

        for (int y = 1; y < rows-1; y++) {
            for (int x = 1; x < cols-1; x++) {
                if (data.get(y).charAt(x) == 'A') {
                    if (((data.get(y-1).charAt(x-1) ^ data.get(y+1).charAt(x+1)) == ('M' ^ 'S')) && ((data.get(y+1).charAt(x-1) ^ data.get(y-1).charAt(x+1)) == ('M' ^ 'S'))) {
                        result += 1;
                    } 
                }
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        long start = System.nanoTime();
        int answer = part2();
        long finish = System.nanoTime();

        System.out.println(answer + ", took: " + ((finish-start) / 1000.0 / 1000.0) + "ms");
    }
}
