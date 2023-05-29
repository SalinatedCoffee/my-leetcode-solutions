class ParkingSystem {
  private int l;
  private int m;
  private int s;

  public ParkingSystem(int big, int medium, int small) {
    l = big;
    m = medium;
    s = small;
  }
  
  public boolean addCar(int carType) {
    switch (carType) {
      case 1:
        if (this.l > 0) {
          this.l--;
          return true;
        } break;
      case 2:
        if (this.m > 0) {
          this.m--;
          return true;
        } break;
      case 3:
        if (this.s > 0) {
          this.s--;
          return true;
        }
    }
    return false;
  }
}
