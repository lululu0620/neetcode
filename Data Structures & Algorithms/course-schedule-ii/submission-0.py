class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degrees = [0] * numCourses
        graph = defaultdict(list)
        for curr, prev in prerequisites:
            degrees[curr] += 1
            graph[prev].append(curr)
        queue = deque()
        for i, degree in enumerate(degrees):
            if degree == 0:
                queue.append(i)
        res = []
        if not queue:
            return []
        while queue:
            for _ in range(len(queue)): 
                curr = queue.popleft()
                res.append(curr)
                for nxt in graph[curr]:
                    degrees[nxt] -= 1
                    if degrees[nxt] == 0:
                        queue.append(nxt)
        return res if len(res) == numCourses else []