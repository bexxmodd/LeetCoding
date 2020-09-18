// https://leetcode.com/problems/move-zeroes/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] nums = {0,1,0,3,12}; // 5

        Solution.moveZeroes(nums);
        for (Integer s: nums) {
            System.out.print(s + ", ");
        }
    }
}

class Solution {
    public static void moveZeroes(int[] nums) {
        int lastNonZeroIndex = 0;

        // Append all non zero elements in the last non
        // zero place
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[lastNonZeroIndex++] = nums[i];
            }
        }
        // Fill the remaining places with zeros
        for (int i = lastNonZeroIndex; i < nums.length; i++) {
            nums[i] = 0;
        }
    }
}
