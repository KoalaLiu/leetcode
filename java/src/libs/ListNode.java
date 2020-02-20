package libs;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/20 21:43
 */

public class ListNode {
    public int val;
    public ListNode next;

    public ListNode(int x) {
        val = x;
    }

    public void PrintChain() {
        ListNode r = this;
        while (r != null) {
            System.out.print(r.val + "->");
            r = r.next;
        }
        System.out.println();
    }
}
