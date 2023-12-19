import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) throws IOException {

        var lines = Files.readAllLines(Paths.get("./input.txt"));
        var star1 = lines.stream().map(line -> {
            var digit = line.replaceAll("[^\\d.]", "");
            return Integer.parseInt(new StringBuilder().append(digit.charAt(0)).append(digit.charAt(digit.length() - 1)).toString());
        }).reduce(0, (a, b) -> a + b);

        var star2 = lines.stream().map(line -> {
            var parsedDigit = repalceSpelledChars(line);
            var digit = parsedDigit.replaceAll("[^\\d.]", "");
            return Integer.parseInt(new StringBuilder().append(digit.charAt(0)).append(digit.charAt(digit.length() - 1)).toString());
        }).reduce(0, (a, b) -> a + b);

         System.out.println(star1);
        System.out.println(star2);
    }

    private static String repalceSpelledChars(String chars) {
        chars = chars.replaceAll("one", "one1one");
        chars = chars.replaceAll("two", "two2two");
        chars = chars.replaceAll("three", "three3three");
        chars = chars.replaceAll("four", "four4four");
        chars = chars.replaceAll("five", "five5five");
        chars = chars.replaceAll("six", "six6six");
        chars = chars.replaceAll("seven", "seven7seven");
        chars = chars.replaceAll("eight", "eight8eight");
        return chars.replaceAll("nine", "nine9nine");
    }
}