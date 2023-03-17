class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    # recursive solution
    return self.recurse(nums, 0, len(nums)-1)
  
  def recurse(self, nums, l, h):
    arr_len = h - l
    arr_mid = (l + h) // 2

    if arr_len < 0:
      return None
    
    # recursively generate left and right subtrees
    left = self.recurse(nums, l, arr_mid-1)
    right = self.recurse(nums, arr_mid+1, h)
    cur = TreeNode(nums[arr_mid], left, right)
    return cur

