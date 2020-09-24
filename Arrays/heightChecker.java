// https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] A = {1,1,4,2,1,3};

        System.out.println(Solution.heightChecker(A));
    }
}

class Solution {
    public static int heightChecker(int[] heights) {
        int[] sortedHeights = new int[heights.length];
        sortedHeights = Arrays.copyOf(heights, heights.length);
        Arrays.sort(sortedHeights);

        int diff = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != sortedHeights[i]) {
                diff++;
            }
        }
        return diff;
    }
}
