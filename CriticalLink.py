from collections import defaultdict
from itertools import count


class CriticalLink:
    def __init__(self):
        self.current_val = 0

    def criticalLink(self, n: int, links: [[int]]) -> int:
        graph = defaultdict(list)
        for vert in links:
            graph[vert[0]].append(vert[1])
            graph[vert[1]].append(vert[0])

        d = [None for i in range(n)]
        low = [None for i in range(n)]
        cur = 0
        start = 0
        result = []

        def dfs(node, parent):
            if d[node] is None:
                d[node] = self.current_val
                low[node] = self.current_val
                self.current_val += 1
                for n in graph[node]:
                    if d[n] is None:
                        dfs(n, node)

                if parent is not None:
                    lw = min([low[i] for i in graph[node] if i != parent] + [low[node]])
                else:
                    lw = min(low[i] for i in graph[node] + [low[node]])
                low[node] = lw

        dfs(0, None)

        for vert in links:
            if low[vert[0]] > d[vert[1]] or low[vert[1]] > d[vert[0]]:
                result.append(vert)
        result = len(result)
        return result

# print(CriticalLink().criticalLink(5, [[1, 0], [0, 2], [2, 1], [0, 3], [3, 4]]))