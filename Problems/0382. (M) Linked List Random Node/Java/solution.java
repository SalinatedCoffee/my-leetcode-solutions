class Solution {
  // naive solution, traverse list twice
  int length = 0;
  ListNode head;
  // Java needs to instantiate object to use prng methods
  Random prng;

  public Solution(ListNode head) {
    this.head = head;
    this.prng = new Random();
    ListNode cur = head;
    // determine length of list
    while (cur.next != null) {
      this.length++;
      cur = cur.next;
    }
  }
  
  public int getRandom() {
    // retrieve random nth node in list
    // nextInt(n) generates int in range [0, n)
    // this.length is 0-indexed so add 1 to n
    int n = this.prng.nextInt(this.length+1);
    ListNode cur = this.head;
    while (n > 0 && cur.next != null) {
      cur = cur.next;
      n--;
    }
    return cur.val;
  }
}
