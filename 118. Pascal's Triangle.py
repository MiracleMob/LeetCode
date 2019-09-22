class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        if numRows == 0:
            return ans
        tmp = []
        for i in range(numRows):
            tmp = [None] * (i + 1)
            tmp[0] = tmp[-1] = 1
            for j in range(1, len(tmp) - 1):
                tmp[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(tmp)
        return ans
