class Solution {
  public int numRescueBoats(int[] people, int limit) {
    // sort, than two pointers

    Arrays.sort(people);
    int lo = 0;
    int hi = people.length - 1;
    int ret = 0;
    while (lo <= hi) {
      // if two people cannot fit, always optimal to ship heaviest person
      if (people[lo]+people[hi] <= limit)
        lo++;
      hi--;
      ret++;
    }
    return ret;
  }
}
