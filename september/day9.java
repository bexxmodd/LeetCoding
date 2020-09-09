// https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/555/week-2-september-8th-september-14th/3454/
// Compare Version Numbers

import java.util.*;

public class Main {

    public static void main(String[] args) {
        String version1 = "1.0.1";
        String version2 = "1";
        System.out.println(Solution.compareVersion(version1, version2)); // 1

        version1 = "7.5.2.4";
        version2 = "7.5.3";
        System.out.println(Solution.compareVersion(version1, version2)); // -1

        version1 = "1.0";
        version2 = "1.0.0";
        System.out.println(Solution.compareVersion(version1, version2)); // 0

        version1 = "1.01";
        version2 = "1.001";
        System.out.println(Solution.compareVersion(version1, version2)); // 0
    }
}

class Solution {
    public static int compareVersion(String version1, String version2) {
        String[] ver1 = version1.split("\\.");
        String[] ver2 = version2.split("\\.");
        int size = ver1.length;
        if (ver2.length < size) {
            size = ver2.length;
        }
        for (int i = 0; i < size; i++) {
            int v1 = Integer.parseInt(ver1[i]);
            int v2 = Integer.parseInt(ver2[i]);
            if (v1 > v2) {
                return 1;
            } else if (v1 < v2) {
                return -1;
            }
        }
        // Check if the extra digit at the end exists and is > 0
        if (ver1.length > ver2.length) {
            int last = Integer.parseInt(ver1[ver1.length - 1]);
            if (last > 0) {
                return 1;
            }
        }
        if (ver1.length < ver2.length) {
            int last = Integer.parseInt(ver2[ver2.length - 1]);
            if (last > 0) {
                return -1;
            }
        }
        return 0;
    }
}
