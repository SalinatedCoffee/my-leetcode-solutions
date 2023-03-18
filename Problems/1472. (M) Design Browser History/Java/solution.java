class BrowserHistory {
  // doubly linked list

  private class HistoryNode {
    String url;
    HistoryNode prev;
    HistoryNode next;

    public HistoryNode(String url) {
      this.url = url;
      this.prev = null;
      this.next = null;
    }

    public HistoryNode(String url, HistoryNode p) {
      this.url = url;
      this.prev = p;
      this.next = null;
    }
  }

  HistoryNode cur;

  public BrowserHistory(String homepage) {
    this.cur = new HistoryNode(homepage);
  }
  
  public void visit(String url) {
    // unlink next node and attach new with url url
    if (this.cur.next != null)
      this.cur.next.prev = null;
    this.cur.next = new HistoryNode(url, this.cur);
    this.cur.next.prev = this.cur;
    this.cur = this.cur.next;
  }
  
  public String back(int steps) {
    // move back steps nodes or until first node is reached
    while (steps > 0 && this.cur.prev != null) {
      this.cur = this.cur.prev;
      steps--;
    }
    return this.cur.url;
  }
  
  public String forward(int steps) {
    // move forward steps nodes or until last node is reached
    while (steps > 0 && this.cur.next != null) {
      this.cur = this.cur.next;
      steps--;
    }
    return this.cur.url;
  }
}
