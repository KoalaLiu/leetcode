/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/22 13:07
 */
public class P0027_RemoveElements {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        for (int j = 0; j < nums.length; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i += 1;
            }
        }
        return i;
    }
}
