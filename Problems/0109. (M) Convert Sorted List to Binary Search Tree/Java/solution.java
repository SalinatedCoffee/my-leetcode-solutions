class Solution {
  // recursive solution with two pointers
  public TreeNode sortedListToBST(ListNode head) {
    if (head == null)
      return null;
    if (head.next == null)
      return new TreeNode(head.val);
    return recurse(head, null);
  }

  private TreeNode recurse(ListNode head, ListNode tail) {
    if (head == tail)
      return null;
    
    ListNode slow = head;
    ListNode fast = head;

    while (fast != tail && fast.next != tail) {
      slow = slow.next;
      fast = fast.next.next;
    }

    // recursively construct subtrees
    TreeNode left = recurse(head, slow);
    TreeNode right = recurse(slow.next, tail);
    return new TreeNode(slow.val, left, right);
  }
}
