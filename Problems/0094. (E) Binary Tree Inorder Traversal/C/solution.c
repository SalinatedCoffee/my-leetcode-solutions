int* inorderTraversal(struct TreeNode* root, int* returnSize) {
  // recursive inorder (LNR) traversal

  // insertion index of current node value, size of return array
  int idx = 0, size = 2;
  int *ans = calloc(size, sizeof(int));
  
  void recurse(struct TreeNode *root, int **returnArray, int *curIdx, int *size) {
    if (root == NULL) return;

    recurse(root->left, returnArray, curIdx, size);

    // realloc return array with double the size whenever necessary
    if (*curIdx == *size) {
      *size *= 2;
      int *re = realloc(*returnArray, *size * sizeof(**returnArray));
      if (re == NULL) return;
      *returnArray = re;
    }
    
    // inorder
    (*returnArray)[(*curIdx)++] = root->val;

    recurse(root->right, returnArray, curIdx, size);
  }

  recurse(root, &ans, &idx, &size);

  *returnSize = idx;
  return ans;
}
