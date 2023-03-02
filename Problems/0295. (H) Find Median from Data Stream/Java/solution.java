class MedianFinder {
  // double heaps

  Queue<Integer> l;
  Queue<Integer> r;

  public MedianFinder() {
    // Java priority queues default to min heaps
    // smaller half, max heap
    this.l = new PriorityQueue(Collections.reverseOrder());
    // larger half, min heap
    this.r = new PriorityQueue();
  }
  
  public void addNum(int num) {
    // both heaps empty
    if (this.l.size() == 0) {
      l.add(num);
      return;
      }
    // if num is smaller than top of smaller half, insert there
    if (num < this.l.peek())
      this.l.add(num);
    else
      this.r.add(num);
    // if size difference is larger than 1, balance
    if (Math.abs(this.l.size() - this.r.size()) > 1) {
      if (this.l.size() > this.r.size()) {
        int temp = this.l.poll();
        this.r.add(temp);
      }
      else {
        int temp = this.r.poll();
        this.l.add(temp);
      }
    }
  }
  
  public double findMedian() {
    // return top of larger heap
    if (this.l.size() > this.r.size())
      return this.l.peek();
    else if (this.r.size() > this.l.size())
      return this.r.peek();
    else
      return (double) (this.l.peek() + this.r.peek()) / 2.0;
  }
}
