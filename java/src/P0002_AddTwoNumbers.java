import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 0:04
 */
public class P0002_AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode res = new ListNode(-1);
        ListNode pHead = res;

        int inc = 0;    // 进位符
        while (l1 != null || l2 != null) {
            int x = l1 != null ? l1.val : 0;
            int y = l2 != null ? l2.val : 0;

            int num = x + y + inc;
            inc = num / 10;

            pHead.next = new ListNode(num % 10);
            pHead = pHead.next;

            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        if (inc > 0) {
            pHead.next = new ListNode(inc);
            // pHead = pHead.next;
        }

        return res.next;
    }
}
