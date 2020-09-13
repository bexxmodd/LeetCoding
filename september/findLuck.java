/* https://leetcode.com/problems/find-lucky-integer-in-an-array/ */

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] arr1 = {2,2,3,4};
        int[] arr2 = {1,2,2,3,3,3};
        int[] arr3 = {2,2,2,3,3};
        int[] arr4 = {1,2,2,3,3,3,4};
        List<int[]> arrays = new ArrayList<>();
        arrays.add(arr1);
        arrays.add(arr2);
        arrays.add(arr3);
        arrays.add(arr4);
        for (int[] a: arrays) {
            System.out.println(Solution.findLucky(a));
        }
    }
}

class Solution {

    public static int findLucky(int[] arr) {
        int lucky = -1;
        HashMap<Integer, Integer> numbers = new HashMap<>();
        for (Integer i: arr) {
            if (numbers.containsKey(i)) {
                numbers.put(i, numbers.get(i) + 1);
            } else {
                numbers.put(i, 1);
            }
        }

        for (int key: numbers.keySet()) {
            System.out.println("key: " + key + " value: " + numbers.get(key));
            if (key == numbers.get(key)
                    && key > lucky) {
                lucky = key;
            }
        }
        return lucky;
    }
}
