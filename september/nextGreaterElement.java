// https://leetcode.com/problems/next-greater-element-i/submissions/

import java.util.*;

public class Main {

    public static void main(String[] args) {
        // Test case #1
        int[] nums1 = {4, 1, 2};
        int[] nums2 = {1, 3, 4, 2};
        int[] sol1 = Solution.nextGreaterElement(nums1, nums2);
        for (Integer i: sol1) {
            System.out.print(i + ", ");
        }

        // Test case #2
        System.out.println();
        int[] nums3 = {2, 4};
        int[] nums4 = {1, 2, 3, 4};
        int[] sol2 = Solution.nextGreaterElement(nums3, nums4);
        for (Integer i: sol2) {
            System.out.print(i + ", ");
        }

        // Test case #3
        System.out.println();
        int[] nums5 = {1, 3, 5, 2, 4};
        int[] nums6 = {6, 5, 4, 3, 2, 1, 7};
        int[] sol3 = Solution.nextGreaterElement(nums5, nums6);
        for (Integer i: sol3) {
            System.out.print(i + ", ");
        }
    }
}

class Solution {
    public static int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] nextGreats = new int[nums1.length];
        for (int i = 0; i < nums1.length; i++) {
            for (int j = 0; j < nums2.length - 1; j++) {
                if (nums1[i] == nums2[j]) {
                    for (int k = j + 1; k < nums2.length; k++) {
                        if (nums1[i] < nums2[k]) {
                            nextGreats[i] = nums2[k];
                            break;
                        }
                    }
                }
            }
            // If we did not find next great value fill with -1
            if (nextGreats[i] == 0) {
                nextGreats[i] = -1;
            }
        }
        return nextGreats;
    }
}
