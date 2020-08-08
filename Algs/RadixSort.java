package SORTING;


public class RadixSort {
    public static void radixSort(int[] nums) {
        if (nums == null || nums.length == 0) return;
        int max = nums[0];
        for (int num : nums) max = Math.max(max, num);

        int exp = 1;
        int R = 10;

        int[] tmp = new int[nums.length];
        while (max / exp > 0) {
            int[] count = new int[R];

            for (int i = 0; i < nums.length; i++) {
                count[nums[i] / exp % 10]++;
            }
            for (int i = 1; i < R; i++) {
                count[i] += count[i-1];
            }
            for (int i = nums.length - 1; i >= 0; i--) {
                tmp[--count[nums[i] / exp % 10]] = nums[i];
            }

            for (int i = 0; i < nums.length; i++) {
                nums[i] = tmp[i];
            }
            exp *= 10;
            for (int num : nums) System.out.printf(num + " ");
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int[] nums = new int[]{5, 31, 37, 130, 127, 189};
        radixSort(nums);
        // for (int num : nums) System.out.printf(num + " ");
    }
}
