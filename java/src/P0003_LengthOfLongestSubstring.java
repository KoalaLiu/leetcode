import java.util.HashSet;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 20:22
 */

public class P0003_LengthOfLongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> set = new HashSet<>();

        int n = s.length();
        int ans = 0, i = 0, j = 0;

        while (i < n && j < n) {
            if (!set.contains(s.charAt(j))) {
                set.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            } else {
                set.remove(s.charAt(i++));
            }

        }

        return ans;
    }

    public static void main(String[] args) {
        P0003_LengthOfLongestSubstring sl = new P0003_LengthOfLongestSubstring();

        String s = "dvdf";
        System.out.println(sl.lengthOfLongestSubstring(s));
    }
}
