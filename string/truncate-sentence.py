class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        w = s.split(" ")
        res = []

        for i in range(k):
            res.append(w[i])
        return " ".join(res)
