import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 16:47
 */

public class P0061_RotateRight {
    public ListNode rotateRight(ListNode head, int k) {
        ListNode p = head;

        while (k > 0) {
            k -= 1;
            if (p == null) {
                p = head;
            } else {
                p = p.next;
            }
        }

        return null;
    }
}
