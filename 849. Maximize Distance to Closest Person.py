class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        st = -1
        for i in range(len(seats)):
            if seats[i] == 1:
                if st == -1:
                    ans = max(i, ans)
                else:
                    ans = max(ans, (i - st) // 2)
                st = i

        ans = max(ans, i - st)

        return ans
