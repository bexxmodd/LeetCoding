// https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] arr = {17,18,5,4,6,1};

        for (Integer i: Solution.replaceElements(arr)) {
            System.out.print(">");
            System.out.print(i + ", ");
        }
    }
}

class Solution {
    public static int[] replaceElements(int[] arr) {
        int maxValue = arr[arr.length - 1];
        for (int i = arr.length - 1; i >= 0; i--) {
            // Put current value in a temp value
            int temp = arr[i];

            // assign to current value max value encountered before
            arr[i] = maxValue;

            // If temp/current value > max value, this becomes max value
            if (temp > maxValue) {
                maxValue = temp;
            }
        }
        // replace last number with -1
        arr[arr.length - 1] = -1;
        return arr;
    }
}
