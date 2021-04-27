class BreadthFirstSearch:
        
    def breadthFirstSearch(self, edges, vertices):
        if vertices == 0:
            return []
        d = {}
        for i in range(vertices):
            d[i] = []
        for i in edges:
            d[i[0]].append(i[1])

        queue = []
        visited = set()
        
        visited.add(0)           ##first visit
        queue.append(0)
        # p = 0
        q = [-1]*vertices
        q[0] = 0
        while queue:
            elem = queue.pop(0)
            # p+=1
            for neigh in d[elem]:
                if neigh not in visited:
                    if q[neigh] == -1:
                        q[neigh] = q[elem] + 1
                    else:
                        temp = q[neigh] + q[elem]
                        if temp < q[neigh]:
                            q[neigh] = temp

                    visited.add(neigh)
                    queue.append(neigh)
                    
        return q




# print(BreadthFirstSearch().breadthFirstSearch([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]],7))
# print(BreadthFirstSearch().breadthFirstSearch([[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]],7))
# print(BreadthFirstSearch().breadthFirstSearch([],0))
# print(BreadthFirstSearch().breadthFirstSearch([],5))
# print(BreadthFirstSearch().breadthFirstSearch([[0,1],[1,0]],3))