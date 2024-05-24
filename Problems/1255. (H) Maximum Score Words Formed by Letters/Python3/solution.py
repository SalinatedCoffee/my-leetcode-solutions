class Solution:
  def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
    # backtracking with dictionaries

    n = len(words)
    # count of remaining letters
    letter_pool = Counter(letters)
    # letter frequency count of each word
    words_freq = [Counter(word) for word in words]
    # total score of each word
    words_score = []
    for f in words_freq:
      total = 0
      for k, v in f.items():
        total += score[ord(k) - ord('a')] * v
      words_score.append(total)

    def recurse(idx):
      # return maximum score for words[idx:]
      # with letter_pool available letters
      # base case
      if idx == n:
        return 0
      # check if words[idx] can be formed with current set of letters
      mismatch = False
      for k, v in words_freq[idx].items():
        if letter_pool[k] < v:
          mismatch = True
          break
      ret = 0
      # if words[idx] can be formed, try selecting it
      if not mismatch:
        for k, v in words_freq[idx].items():
          letter_pool[k] -= v
        ret = words_score[idx] + recurse(idx + 1)
        for k, v in words_freq[idx].items():
          letter_pool[k] += v

      # try skipping words[idx]
      return max(ret, recurse(idx + 1))

    return recurse(0)

