class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = []
        while n > 0:
            ans.append(n%2)
            n = (n - n%2) / 2
        t = 1
        res = 0
        ans.extend([0] * (32-len(ans)))
        for i in range(len(ans)-1, -1, -1):
            res += ans[i] * t
            t = t * 2
        return res