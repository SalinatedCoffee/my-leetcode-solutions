class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping = {}
        words = s.split()
        if len(pattern) != len(words):
          return False

        for p, word in zip(pattern, words):
            if p in mapping:
                if mapping[p] != word:
                    return False
            else:
                if word in mapping.values():
                    return False
            mapping[p] = word
        return True

