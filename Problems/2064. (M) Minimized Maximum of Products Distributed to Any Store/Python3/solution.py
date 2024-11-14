class Solution:
  def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
    # greedy algorithm using max heap
    
    m = len(quantities)
    # max heap containing tuples (maximum stock among stores stocking i-th product, i)
    category_max = [(-quantities[i], i) for i in range(m)]
    heapify(category_max)
    # number of stores currently stocking each product type
    alloc_stores = [1] * m
    # initially stock each product type at 1 store
    n -= m
    while n:
      _, idx = heappop(category_max)
      alloc_stores[idx] += 1
      new_max = -ceil(quantities[idx] / alloc_stores[idx])
      heappush(category_max, (new_max, idx))
      n -= 1

    return -category_max[0][0]

