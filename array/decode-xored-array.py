class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]

        for e in encoded:
            result.append(result[-1] ^ e)

        return result