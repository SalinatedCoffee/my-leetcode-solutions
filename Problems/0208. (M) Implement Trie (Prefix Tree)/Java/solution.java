class Trie {
  // naive trie implementation using arrays of length 26
  class TrieNode {
    TrieNode[] children = new TrieNode[26];
    boolean last = false;

    public TrieNode() {
    }
  }

  TrieNode root = new TrieNode();

  public Trie() {
  }
  
  public void insert(String word) {
    TrieNode cur = this.root;
    for (int i = 0; i < word.length(); i++) {
      // implicit type casting
      int idx = word.charAt(i) - 'a';
      if (cur.children[idx] == null)
        cur.children[idx] = new TrieNode();
      cur = cur.children[idx];
    }
    cur.last = true;
  }
  
  public boolean search(String word) {
    TrieNode cur = this.root;
    for (int i = 0; i < word.length(); i++) {
      int idx = word.charAt(i) - 'a';
      if (cur.children[idx] == null)
        return false;
      cur = cur.children[idx];
    }
    return cur.last;
  }
  
  public boolean startsWith(String prefix) {
    TrieNode cur = this.root;
    for (int i = 0; i < prefix.length(); i++) {
      int idx = prefix.charAt(i) - 'a';
      if (cur.children[idx] == null)
        return false;
      cur = cur.children[idx];
    }
    return true;
  }
}
