/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/22 20:54
 */
public class P0053_MaxSubArray {
    public int maxSubArray(int[] nums) {
        int ans = nums[0];
        int sum = 0;
        for (int num : nums) {
            if (sum > 0) {
                sum += num;
            } else {
                sum = num;
            }

            ans = Math.max(ans, sum);
        }

        return ans;
    }
}
