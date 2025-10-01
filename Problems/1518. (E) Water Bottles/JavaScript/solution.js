var numWaterBottles = function(numBottles, numExchange) {
  // simulation
  let res = 0;
  let empty = 0;
  while (numBottles > 0) {
    // drink bottle and update values accordingly
    res++;
    empty++;
    numBottles--;
    // exchange empty bottles when possible
    if (empty === numExchange) {
      empty = 0;
      numBottles++;
    }
  }
  return res;
};

