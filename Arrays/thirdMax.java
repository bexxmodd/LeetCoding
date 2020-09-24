// https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        int[] A = {2, 2, 3, 1};
        int[] B = {5, 2, 2};
        int[] J = {3, 2, 1};
        int[] C = {1, 2, 2, 5, 3, 1};

        System.out.println(Solution.thirdMax(A)); // 1
        System.out.println(Solution.thirdMax(B)); // 5
        System.out.println(Solution.thirdMax(J)); // 1
        System.out.println(Solution.thirdMax(C)); // 2
    }
}

class Solution {
    public static int thirdMax(int[] nums) {
        if (nums.length < 3) {
            return Math.max(nums[0], nums[1]);
        }
        Arrays.sort(nums);
        int thirdMax = 0;
        int counter = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                thirdMax = nums[i];
                counter++;
            }
            if (counter == 3) {
                return thirdMax;
            }
        }
        return nums[nums.length - 1];
    }
}
