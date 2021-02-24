import java.util.*;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        
        List<Integer> listOfNumbers = new ArrayList<>();
        int[] duplicates = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (duplicates[nums[i] - 1] == 0) {
                duplicates[nums[i] - 1] = 1;
            } else {
                listOfNumbers.add(nums[i]);
            }
        }
        return listOfNumbers;
    }
}