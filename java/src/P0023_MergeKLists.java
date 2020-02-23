import libs.ListNode;

/**
 * @author KoalaLiu
 * @version 1.0
 * @date 2020/2/23 8:59
 */

public class P0023_MergeKLists {
    private ListNode findMinList(ListNode[] lists, boolean[] nullIndex) {
        int minValue = Integer.MAX_VALUE;
        int minListIndex = -1;
        for (int i = 0; i < nullIndex.length; i++) {
            if (!nullIndex[i]) {
                ListNode l = lists[i];

                if (l == null) {
                    nullIndex[i] = true;
                    continue;
                }

                if (l.val <= minValue) {
                    minValue = l.val;
                    minListIndex = i;
                }
            }
        }

        if (minListIndex == -1) {
            return null;
        } else {
            ListNode res = lists[minListIndex];
            lists[minListIndex] = lists[minListIndex].next;
            return res;
        }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        ListNode res = new ListNode(-1);
        ListNode pHead = res;

        boolean[] nullIndex = new boolean[lists.length];

        while (true) {
            ListNode minNode = findMinList(lists, nullIndex);
            if (minNode == null) {
                pHead.next = null;
                break;
            }

            pHead.next = minNode;
            pHead = pHead.next;
        }

        return res.next;
    }

    public static void main(String[] args) {
        P0023_MergeKLists s = new P0023_MergeKLists();
        ListNode l1 = new ListNode(1);
        l1.next = new ListNode(2);
        l1.next.next = new ListNode(3);
        l1.next.next.next = new ListNode(4);

        ListNode l2 = new ListNode(4);
        l2.next = new ListNode(5);
        l2.next.next = new ListNode(6);

        ListNode l3 = new ListNode(7);
        l3.next = new ListNode(8);
        l3.next.next = new ListNode(9);

        ListNode[] input = {l1, l2, l3};
        ListNode r = s.mergeKLists(input);
        r.PrintChain();
    }
}
