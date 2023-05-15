class Solution {
  public ListNode swapNodes(ListNode head, int k) {
    // cast list to array and swap values

    List<ListNode> nodes = new ArrayList();
    ListNode cur = head;
    while (cur != null) {
      nodes.add(cur);
      cur = cur.next;
    }
    int k_r = nodes.size() - k;
    k--;
    int temp = nodes.get(k_r).val;
    nodes.get(k_r).val = nodes.get(k).val;
    nodes.get(k).val = temp;
    return head;
  }
}
