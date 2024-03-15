var productExceptSelf = function(nums) {
  // pre/suffix products
  // same logic as Python/Java solutions/
  // but suffix products computed in seperate run

  let n = nums.length;
  let pre = [], suf = [];
  let prod = 1;
  // compute prefix products
  for (num of nums) {
    prod *= num;
    pre.push(prod);
  }
  prod = 1;
  // compute suffix products
  for (num of nums.reverse()) {
    prod *= num;
    suf.push(prod);
  }
  suf.reverse();
  let ret = [];
  // compute products excluding each element of nums
  ret.push(suf[1]);
  for (let i = 1; i < n-1; i++) ret.push(pre[i-1] * suf[i+1]);
  ret.push(pre[n-2]);
  return ret;
};
