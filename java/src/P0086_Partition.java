import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 15:56
 */
public class P0086_Partition {
    public ListNode partition(ListNode head, int x) {
        if (head == null) return null;

        ListNode dummyLt = new ListNode(-1);
        ListNode dummyGt = new ListNode(-1);

        ListNode p1 = dummyLt;
        ListNode p2 = dummyGt;

        while (head != null) {
            if (head.val < x) {
                p1.next = head;
                p1 = p1.next;
            } else {
                p2.next = head;
                p2 = p2.next;
            }
            head = head.next;
        }

        p1.next = dummyGt.next;
        p2.next = null;
        return dummyLt.next;
    }

    public static void main(String[] args) {
        P0086_Partition s = new P0086_Partition();

        ListNode n = new ListNode(1);
        n.next = new ListNode(4);
        n.next.next = new ListNode(3);
        n.next.next.next = new ListNode(2);
        n.next.next.next.next = new ListNode(5);
        n.next.next.next.next.next = new ListNode(2);

        ListNode res = s.partition(n, 3);
        res.PrintChain();
    }
}
