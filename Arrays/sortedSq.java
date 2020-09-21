// https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3261/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] A = {-4,-1,0,3,10};

        int[] Sol = Solution.sortedSquares(A);
        for (Integer a: Sol) {
            System.out.print(a + ", ");
        }
    }
}

class Solution {
    public static int[] sortedSquares(int[] A) {
        int[] sortedSq = new int[A.length];

        for (int i = 0; i < A.length; i++) {
            sortedSq[i] = A[i] * A[i];
        }
        Arrays.sort(sortedSq);
        return sortedSq;
    }
}
