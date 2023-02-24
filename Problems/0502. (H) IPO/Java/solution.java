class Solution {
  public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
    // use sorted list with heap to store project pool

    // sort projects by capital
    // manually zip items in a Pair and sort
    Pair<Integer,Integer>[] projects = new Pair[profits.length];
    for (int i = 0; i < profits.length; i++)
      projects[i] = new Pair<Integer,Integer>(capital[i], profits[i]);
    // need to define custom comparator for Java Pairs
    Arrays.sort(projects, (p1, p2) -> p1.getKey().compareTo(p2.getKey()));

    // available projects at a given time
    // Java pri. queues are min-heaps but also supports max-heaps
    Queue<Integer> avail_proj = new PriorityQueue<>(Collections.reverseOrder());
    // index pointint to first unavailable project
    int unavail = 0;

    for (int i = 0; i < k; i++) {
      while (unavail < projects.length && w >= projects[unavail].getKey()) {
        avail_proj.add(projects[unavail].getValue());
        unavail += 1;
      }
      // no more projects available
      if (avail_proj.size() == 0)
        break;
      // do available project
      w += avail_proj.poll();
    }
    return w;
  }
}
