/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/22 22:42
 */
public class P0066_PlusOne {
    public int[] reduceDigits(int[] digits) {
        if (digits[0] != 0) {
            return digits;
        }

        int[] res = new int[digits.length - 1];
        for (int i = 0, j = 1; j < digits.length; i++, j++) {
            res[i] = digits[j];
        }

        return res;
    }

    public int[] plusOne(int[] digits) {
        int[] res = new int[digits.length + 1];

        int inc = 1;
        for (int i = digits.length - 1; i >= 0; i--) {
            int num = digits[i] + inc;
            res[i + 1] = num % 10;
            inc = num / 10;
        }
        res[0] = inc;

        return reduceDigits(res);
    }
}
