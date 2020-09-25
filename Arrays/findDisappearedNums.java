// https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] A = {4,3,2,7,8,2,3,1};
        int[] B = {5, 2, 2};

        System.out.println(Solution.findDisappearedNumbers(A)); // [5, 6]
//        System.out.println(Solution.findDisappearedNumbers(B)); // 5
    }
}

class Solution {
    public static List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> disaps = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            int val = Math.abs(nums[i]) - 1;
            if (nums[val] > 0) {
                nums[val] = -nums[val];
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                disaps.add(i + 1);
            }
        }
        return disaps;
    }
}
