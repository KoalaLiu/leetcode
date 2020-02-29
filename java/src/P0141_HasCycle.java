import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 15:31
 */

public class P0141_HasCycle {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;

        ListNode p1 = head;
        ListNode p2 = head;

        while (true) {
            if (p1 == null || p2 == null || p2.next == null) {
                return false;
            }

            p1 = p1.next;
            p2 = p2.next.next;
            if (p1 == p2) {
                return true;
            }
        }
    }
}
