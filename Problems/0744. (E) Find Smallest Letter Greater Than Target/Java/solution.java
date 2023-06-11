class Solution {
  public char nextGreatestLetter(char[] letters, char target) {
    // binary search;

    int lo = 0;
    int hi = letters.length - 1;
    int mid;
    while (lo <= hi) {
      mid = (lo + hi) / 2;
      if (letters[mid] > target)
        hi = mid-1;
      else
        lo = mid+1;
    }
    return lo != letters.length ? letters[lo] : letters[0];
  }
}
