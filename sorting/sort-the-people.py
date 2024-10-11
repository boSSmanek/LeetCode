class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        sorted_heights = sorted(zip(heights, names), reverse=True)
       
        res = [n for h, n in sorted_heights]
        return res