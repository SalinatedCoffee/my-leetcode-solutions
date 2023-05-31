class UndergroundSystem {
  // nested dictionaries
  private Map<Integer,Pair<String,Integer>> passengers;
  private Map<String,Map<String,Pair<Integer,Integer>>> stations;
  public UndergroundSystem() {
    this.passengers = new HashMap();
    this.stations = new HashMap();
  }
  
  public void checkIn(int id, String stationName, int t) {
    if (!this.passengers.containsKey(id))
      this.passengers.put(id, new Pair(stationName, t));
  }
  
  public void checkOut(int id, String stationName, int t) {
    if (this.passengers.containsKey(id)) {
      Pair<String,Integer> origin = this.passengers.get(id);
      int duration = t - origin.getValue();
      if (!this.stations.containsKey(stationName))
        this.stations.put(stationName, new HashMap());
      if (!this.stations.get(stationName).containsKey(origin.getKey()))
        this.stations.get(stationName).put(origin.getKey(), new Pair(duration, 1));
      else {
        Pair<Integer,Integer> temp = this.stations.get(stationName).get(origin.getKey());
        int d_sum = temp.getKey() + duration;
        int traffic = temp.getValue() + 1;
        this.stations.get(stationName).put(origin.getKey(), new Pair(d_sum, traffic));
      }
      this.passengers.remove(id);
    }
  }
  
  public double getAverageTime(String startStation, String endStation) {
    if (this.stations.containsKey(endStation)) {
      if (this.stations.get(endStation).containsKey(startStation)) {
        Pair<Integer,Integer> stats = this.stations.get(endStation).get(startStation);
        return (double) stats.getKey() / stats.getValue();
      }
    }
    // this line should never run given problem constraints
    return Double.MAX_VALUE;
  }
}
