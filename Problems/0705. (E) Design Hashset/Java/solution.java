class MyHashSet {
  // store all elements in 2D list

  private List<Integer>[] items;
  private boolean max;

  public MyHashSet() {
    this.items = new List[1000];
    for (int i = 0; i < 1000; i++)
      this.items[i] = new ArrayList();
    this.max = false;
  }
  
  public void add(int key) {
    if (key == 1000000)
      this.max = true;
    else {
      int mod = key % 1000;
      int quot = key / 1000;
      if (!this.contains(key))
        this.items[quot].add(mod);
    }
  }
  
  public void remove(int key) {
    if (key == 1000000)
      this.max = false;
    else {
      int mod = key % 1000;
      int quot = key / 1000;
      this.items[quot].remove(new Integer(mod));
    }
  }
  
  public boolean contains(int key) {
    if (key == 1000000)
      return this.max;
    int mod = key % 1000;
    int quot = key / 1000;
    return this.items[quot].contains(mod);
  }
}
