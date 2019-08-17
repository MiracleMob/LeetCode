class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 递减栈,逆序遍历
        # 对于[75,71,69,72,76,73],从后往前减少遍历次数；对于75,
        # 可以根据71的结果=2，找到栈顶元素72，而72比75小，pop，找到72的结果76；则75的结果元素是76，即76.index -
        #  75.index
        stack = []
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans

