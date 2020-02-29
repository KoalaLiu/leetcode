/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/25 23:22
 */
public class P0012_IntToRoman {
    public String intToRoman(int num) {
        int[] numbers = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] numSymbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

        StringBuilder sb = new StringBuilder();
        while (num > 0) {
            for (int i = 0; i < numbers.length; i++) {
                if (numbers[i] <= num) {
                    num -= numbers[i];
                    sb.append(numSymbols[i]);
                    break;
                }
            }
        }

        return sb.toString();
    }
}
