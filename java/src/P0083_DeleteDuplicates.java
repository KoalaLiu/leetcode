import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 14:31
 */

public class P0083_DeleteDuplicates {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode res = head;
        ListNode prev = head;
        head = head.next;
        while (head != null) {
            if (head.val == prev.val) {
                prev.next = head.next;
            } else {
                prev = head;
            }

            head = head.next;
        }

        return res;
    }
}
