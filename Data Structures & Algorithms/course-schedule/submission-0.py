class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        
        inDegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            inDegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            course = q.popleft()
            count += 1
            for post in graph[course]:
                inDegree[post] -= 1
                if inDegree[post] ==0:
                    q.append(post)

        return (count == numCourses)