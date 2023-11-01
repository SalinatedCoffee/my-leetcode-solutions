class Solution:
  def findMode(self, root: Optional[TreeNode]) -> List[int]:
    # full traversal

    freq = Counter()

    nodes = [root]
    while nodes:
      cur = nodes.pop()
      freq[cur.val] += 1
      if cur.left:
        nodes.append(cur.left)
      if cur.right:
        nodes.append(cur.right)
    
    freq = sorted([(v,k) for k,v in freq.items()], reverse=True, key=lambda x: x[0])
    ret = []
    m = freq[0][0]
    for v, k in freq:
      if v == m:
        ret.append(k)
      else:
        break

    return ret

