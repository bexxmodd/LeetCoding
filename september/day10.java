//https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3455/


public class Main {

    public static void main(String[] args) {
        String secret = "1807";
        String guess = "7810";
        System.out.println(Solution.getHint(secret, guess));

        String secret1 = "1123";
        String guess1 = "0111";
        System.out.println(Solution.getHint(secret1, guess1));

        String secret2 = "1122";
        String guess2 = "2211";
        System.out.println(Solution.getHint(secret2, guess2));
    }
}

class Solution {
    public static String getHint(String secret, String guess) {
        int[] counts = new int[10];
        int bulls = 0;
        int cows = 0;

        for (int i = 0; i < secret.length(); i++) {
            counts[secret.charAt(i) - 48]++;
            if (guess.charAt(i) == secret.charAt(i)) {
                bulls++;
                counts[secret.charAt(i) - 48]--;
            }
        }

        for (int i = 0; i < secret.length(); i++) {
            if (guess.charAt(i) != secret.charAt(i)
                    && counts[guess.charAt(i) - 48] > 0) {
                cows++;
                counts[guess.charAt(i) - 48]--;
            }
        }
        return bulls + "A" + cows + "B";
    }
}
