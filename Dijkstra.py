class Dijkstra:
    def shortestDistance(self, edges, vertices):
        if vertices ==0:
            return []
        graph = {}
        for i in range(vertices):
            graph[i] = {}
        for i in edges:
            graph[i[0]][i[1]] = i[2]
        final = [-1]*vertices
        shortest_distance = {}
        for node in graph:
            shortest_distance[node] = float('inf')
        shortest_distance[0] = 0

        while graph:
            minNode = None
            for node in graph:
                if minNode is None:
                    minNode = node
                elif shortest_distance[node]<shortest_distance[minNode]:
                    minNode = node
            for neigh,wt in graph[minNode].items():
                if wt+shortest_distance[minNode]<shortest_distance[neigh]:
                    shortest_distance[neigh] = wt+shortest_distance[minNode]
                    final[neigh] = wt+shortest_distance[minNode]
            graph.pop(minNode)
        final[0] = 0
        
        
        return final













# vertices = 6
# edges = [[0, 1, 4], [0, 2, 2], [1, 3, 2], [1, 4, 3], [2, 1, 1], [2, 3, 2], [2, 4, 5], [4, 3, 1], [5, 2, 2]]
# print(Dijkstra().shortestDistance(edges,vertices))
