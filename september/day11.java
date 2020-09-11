//https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3456/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] nums1 = {2, 3, -2, 4};
        System.out.println(Solution.maxProduct(nums1));

        int[] nums2 = {-2, 0, -1};
        System.out.println(Solution.maxProduct(nums2));
    }
}

class Solution {
    public static int maxProduct(int[] nums) {
        int[] max = new int[nums.length];
        int[] min = new int[nums.length];

        max[0] = min[0] = nums[0];
        int result = nums[0];

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > 0) {
                max[i] = Math.max(nums[i], max[i - 1] * nums[i]);
                min[i] = Math.min(nums[i], min[i - 1] * nums[i]);
            } else {
                max[i] = Math.max(nums[i], min[i - 1] * nums[i]);
                min[i] = Math.min(nums[i], max[i - 1] * nums[i]);
            }

            if (max[i] > result) {
                result = max[i];
            }
        }
        return result;
    }
}
