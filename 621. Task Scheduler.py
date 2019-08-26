class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        length = len(tasks)
        if length <= 1:
            return length
        task_map = {}
        for task in tasks:
            if task not in task_map:
                task_map[task] = 1
            else:
                task_map[task] += 1
        task_list = sorted(task_map.items(), key=lambda x: x[1], reverse=True)

        # 出现次数最多的任务
        max_cnt = task_list[0][1]
        ans = (max_cnt - 1) * (n + 1)
        for task in task_list:
            if task[1] == max_cnt:
                ans += 1
        return ans if ans >= length else length