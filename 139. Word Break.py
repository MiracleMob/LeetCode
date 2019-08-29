class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # BFS
        queue = []
        queue.append(0)
        visited = [0] * len(s)
        while queue:
            st = queue.pop(0)
            if visited[st] == 0:
                for ed in range(st, len(s)):
                    if s[st:ed + 1] in wordDict:
                        queue.append(ed + 1)
                        if ed == len(s) - 1:
                            return True
            visited[st] = 1

        return False


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # dp
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[-1]
