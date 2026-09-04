class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int min = nums[0], max = nums[0];
        for (int i : nums) {
            min = Math.min(i, min);
            max = Math.max(i, max);
        }
        return Math.max(0, max - min - 2 * k);
    }
}