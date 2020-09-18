# https://leetcode.com/problems/valid-mountain-array/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] arr = {2,1};
        int[] arr2 = {3,5,5};
        int[] arr3 = {0,3,2,1};
        int[] arr4 = {-10,12,-20,-8,15};
        int[] arr5 = {-2,0,10,-19,4,6,-8};
        int[] arr6 = {1,3,4,5,6,4,3,1};

        System.out.println(Solution.validMountainArray(arr));
        System.out.println(Solution.validMountainArray(arr2));
        System.out.println(Solution.validMountainArray(arr3));
        System.out.println(Solution.validMountainArray(arr4));
        System.out.println(Solution.validMountainArray(arr5));
        System.out.println(Solution.validMountainArray(arr6));
    }
}

class Solution {
    public static boolean validMountainArray(int[] A) {
        // check if A has a valid length
        int N = A.length;
        int i = 0;

        // walk up
        while (i + 1 < N && A[i] < A[i + 1]) {
            i++;
        }

        // peak can't be first of last
        if (i == 0 || i == N - 1) {
            return false;
        }

        // walk down
        while (i + 1 < N && A[i] > A[i + 1]) {
            i++;
        }

        return i == N - 1;
    }
}
