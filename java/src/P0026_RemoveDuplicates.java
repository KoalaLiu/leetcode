/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/22 0:16
 */
public class P0026_RemoveDuplicates {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 0) {
            return 0;
        }

        int i = 0;
        for (int j = 1; j < nums.length; j++) {
            if (nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }

    public static void main(String[] args) {
        P0026_RemoveDuplicates s = new P0026_RemoveDuplicates();

        int[] nums = {0, 0, 1, 1, 1, 2, 2, 3, 3, 4};
        int len = s.removeDuplicates(nums);
        for (int i = 0; i < len; i++) {
            System.out.print(nums[i] + " ");
        }

    }
}
