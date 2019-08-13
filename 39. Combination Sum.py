class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        n = len(candidates)

        def backtrack(index, tmpsum, tmp):
            if index == n or tmpsum > target:
                return
            if tmpsum == target:
                ans.append(tmp)
                return

            for j in range(index, n):
                backtrack(j, tmpsum + candidates[j], tmp + [candidates[j]])

        backtrack(0, 0, [])

        return ans



