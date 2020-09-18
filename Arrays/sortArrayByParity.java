// https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] A = {3,1,2,4}; // 5

        int[] Sol = Solution.sortArrayByParity(A);
        for (Integer a: Sol) {
            System.out.print(a + ", ");
        }
    }
}

class Solution {
    public static int[] sortArrayByParity(int[] A) {
        int[] sorted = new int[A.length];
        int evenPointer = 0;
        int oddPointer = A.length - 1;

        for (int i = 0; i < A.length; i++) {
            // Append evens from the start
            // Evens from the ned
            if (A[i] % 2 == 0) {
                sorted[evenPointer++] = A[i];
            } else {
                sorted[oddPointer--] = A[i];
            }
        }
        return sorted;
    }
}
