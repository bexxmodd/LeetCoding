/* https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/ */

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] arr = {10,2,5,3};
        int[] arr2 = {7,1,14,11};
        int[] arr3 = {3,1,7,11};
        int[] arr4 = {-10,12,-20,-8,15};
        int[] arr5 = {-2,0,10,-19,4,6,-8};

        System.out.println(Solution.checkIfExist(arr));
        System.out.println(Solution.checkIfExist(arr2));
        System.out.println(Solution.checkIfExist(arr3));
        System.out.println(Solution.checkIfExist(arr4));
        System.out.println(Solution.checkIfExist(arr5));
    }
}

class Solution {

    public static boolean checkIfExist(int[] arr) {

        for (int i = 0; i < arr.length ; i++) {
            for (int j = 0; j < arr.length; j++) {
                if (arr[i] == arr[j] * 2
                        && i != j) {
                    return true;
                }
            }
        }
        return false;
    }
}
