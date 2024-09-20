class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        f = word.find(ch)
        w = word[:f + 1]
        result = ""
        if f + 1 < len(word):
            result = word[f + 1:]
        
        w = w[::-1]
        return w + result