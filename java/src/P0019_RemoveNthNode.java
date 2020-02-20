import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/20 21:43
 */
public class P0019_RemoveNthNode {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummpy = new ListNode(0);
        dummpy.next = head;
        ListNode first = head;
        int len = 0;
        while (first != null) {
            len += 1;
            first = first.next;
        }

        first = dummpy;
        len -= n;
        while (len > 0) {
            len -= 1;
            first = first.next;
        }
        first.next = first.next.next;

        return dummpy.next;
    }

    public ListNode removeNthFromEnd2(ListNode head, int n) {
        ListNode dummpy = new ListNode(0);
        dummpy.next = head;

        ListNode p1 = dummpy;
        ListNode p2 = dummpy;

        for (int i = 0; i <= n; i++) {
            p2 = p2.next;
        }

        while (p2 != null) {
            p2 = p2.next;
            p1 = p1.next;
        }
        p1.next = p1.next.next;

        return dummpy.next;
    }

    public static void main(String[] args) {
        ListNode node = new ListNode(0);
        node.next = new ListNode(1);
        node.next.next = new ListNode(2);
        node.next.next.next = new ListNode(3);
        node.next.next.next.next = new ListNode(4);
        node.PrintChain();

        node = new ListNode(1);
        node.PrintChain();

        P0019_RemoveNthNode solution = new P0019_RemoveNthNode();
//        ListNode newNode = solution.removeNthFromEnd(node, 2);
        ListNode newNode2 = solution.removeNthFromEnd2(node, 2);
//        newNode.PrintChain();
        newNode2.PrintChain();
    }
}
