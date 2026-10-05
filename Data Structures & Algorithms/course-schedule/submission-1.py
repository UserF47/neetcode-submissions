from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(int)
        for c in range(numCourses):
            graph[c] = {'pre': 0, 'post':[]}
        
        for preq in prerequisites:
            graph[preq[0]]['pre'] += 1
            graph[preq[1]]['post'].append(preq[0])

        q = deque()

        for c in graph:
            if graph[c]['pre'] == 0:
                q.append(c)
                numCourses -= 1

        while q:
            c = q.popleft()
            for p in graph[c]['post']:
                graph[p]['pre'] -= 1
                if graph[p]['pre'] == 0:
                    q.append(p)
                    numCourses -= 1

        return True if numCourses == 0 else False






        