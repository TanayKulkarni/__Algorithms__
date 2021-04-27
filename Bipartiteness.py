class Bipartiteness:

    def bipartite(self, edges, v):
        if v == 0 or v == 1:
            return 1
        self.graph = {x : [] for x in range(v)}
        self.add_edges(edges)
        return self.bfs(v)

    def add_edges(self, edges):
        for n1, n2 in edges:
            self.graph[n1].append(n2)
            self.graph[n2].append(n1)
    
    def successor(self, n):
        return self.graph[n]

    def bfs(self, v):
        color = [-1 for x in range(v)]
        fringe = []
        for i in range(v):
            if color[i] == -1:
                fringe.append((i, 0))
                color[i] = 0

                while fringe:
                    n, col = fringe.pop(0)
                    for succ in self.graph[n]:
                        if color[succ] == col:
                            return -1
                        if color[succ] == -1:
                            color[succ] = 1 - col
                            fringe.append((succ, color[succ]))
        return 1

# vertices = 7
# edges = [[0, 6], [1, 6], [1, 2], [5, 6], [3, 2], [3, 4], [6, 2]]

# print(Bipartiteness().bipartite(edges,vertices))