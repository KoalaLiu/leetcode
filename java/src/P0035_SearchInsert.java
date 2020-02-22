/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/22 13:31
 */
public class P0035_SearchInsert {
    public int searchInsert(int[] nums, int target) {
        int i = 0;
        while (i < nums.length) {
            if (target <= nums[i]) {
                return i;
            }
            i++;
        }
        return i;
    }
}
