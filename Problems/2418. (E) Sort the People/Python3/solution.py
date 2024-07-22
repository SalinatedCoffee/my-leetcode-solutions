class Solution:
  def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    # sorting
    
    return [names[idx] for idx in sorted([i for i in range(len(names))], key=lambda x: heights[x], reverse=True)]

