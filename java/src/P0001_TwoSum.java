import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/21 21:10
 */
public class P0001_TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mp = new TreeMap<>();

        for (int i = 0; i < nums.length; i++) {
            int needed = target - nums[i];
            int targetIndex = mp.getOrDefault(needed, -1);
            if (targetIndex != -1) {
                return new int[] {targetIndex, i};
            }

            mp.put(nums[i], i);
        }

        return null;
    }


    public static void main(String[] args) {

    }
}
