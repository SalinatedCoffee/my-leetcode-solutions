class WordDictionary {
  // prefix tree (trie) that supports wildcard search
  Node root;
  int max_length;

  class Node {
    Node[] children;
    boolean last;

    public Node() {
      children = new Node[26];
      last = false;
    }
  }

  public WordDictionary() {
    root = this.new Node();
    // since WordDictionary doesn't support delete
    // keep track of length of longest word
    max_length = 0;
  }
  
  public void addWord(String word) {
    // iteratively add word to trie

    Node cur = this.root;
    int idx;
    for (int i = 0; i < word.length(); i++) {
      idx = (int) word.charAt(i) - (int) 'a';
      if (cur.children[idx] == null)
        cur.children[idx] = this.new Node();
      cur = cur.children[idx];
    }
    cur.last = true;
    this.max_length = Math.max(this.max_length, word.length());
  }
  
  public boolean search(String word, Node... node) {
    // sanity check
    if (word.length() > this.max_length)
      return false;

    Node cur = this.root;
    // some weirdness going on with Varargs
    // apparently Node... is just syntactic sugar for Node[]
    if (node.length == 1)
      cur = node[0];

    int idx = 0;
    for (int i = 0; i < word.length(); i++) {
      if (word.charAt(i) == '.') {
        boolean ret = false;
        for (int j = 0; j < 26; j++) {
          // recurse on wildcards
          if (cur.children[j] != null)
            ret |= search(word.substring(i+1), cur.children[j]);
        }
        return ret;
      }
      idx = (int) word.charAt(i) - (int) 'a';
      if (cur.children[idx] == null)
        return false;
      cur = cur.children[idx];
    }
    return cur.last;
  }
}
