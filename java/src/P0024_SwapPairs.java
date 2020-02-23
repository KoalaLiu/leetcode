import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 13:32
 */

public class P0024_SwapPairs {
    public ListNode swapPairs(ListNode head) {
        if (head == null) {
            return null;
        }

        // dummy (pHead)
        ListNode dummy = new ListNode(-1);
        dummy.next = head;

        ListNode prev = dummy;
        while (head != null && head.next != null) {
            ListNode first = head;
            ListNode second = head.next;

            prev.next = second;
            first.next = second.next;
            second.next = first;

            prev = first;
            head = prev.next;
        }

        return dummy.next;
    }
}
