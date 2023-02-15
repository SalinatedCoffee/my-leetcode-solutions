class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1: return True

        first = True
        for i in range(1, len(word)):
            if first:
                if not word[i-1].isupper() and word[i].isupper():
                    return False
                first = False
            else:
                if word[i-1].isupper() != word[i].isupper():
                    return False
        return True

