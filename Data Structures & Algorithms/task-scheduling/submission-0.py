# # we loop from time slot 1 to where it stops
# At slot i we want to choose:
# 1. eligible task (following rule: identical tasks must be separated by at least n CPU cycles)
# 2. repeated most in the remaining task, as we want to start those as early as possible

# how to choose a task that repeats most in the remaining tasks -> max heap 
# where to keep the cooling down task -> queue, after n slots, it becomes eligible again, we push it to the heap

# create counter varible to keep a trace of #time slots
# while loop stops when both heap and queue are empty

from collections import deque, Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter_heap = [] 
        waiting_queue = deque()
        time_solt_counter = 0

        each_task_repeat_times = [-c for c in Counter(tasks).values()]
        for each_task in each_task_repeat_times:
            heapq.heappush(task_counter_heap, each_task)

        while task_counter_heap or waiting_queue:
            if waiting_queue:
                head_waiting_queue = waiting_queue[0]
                if head_waiting_queue[1] == time_solt_counter:
                    waiting_queue.popleft()
                    heapq.heappush(task_counter_heap, head_waiting_queue[0])

            if not task_counter_heap:
                time_solt_counter += 1
                continue

            most_repeat = heapq.heappop(task_counter_heap)
            if most_repeat+1 != 0:
                waiting_queue.append((most_repeat+1, time_solt_counter + n + 1))

            time_solt_counter += 1
        
        return time_solt_counter












