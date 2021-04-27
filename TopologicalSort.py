class TopologicalSort:
        def topoSort(self, pre_requisites: [[int]], total_courses: int) -> [int]:   
            print(pre_requisites)
            d = {}
            s = set()
            for i in range(total_courses):
                d[i] = []
            for arr in pre_requisites:
                d[arr[0]].append(arr[1])
            print(d)
            op = []
            for i in range(total_courses):
                self.visit(i,d,s,op)
            print(op)
            return op
        def visit(self,vertex,d,s,op):
            if vertex not in s:
                s.add(vertex)
                for neigh in d[vertex]:
                    self.visit(neigh, d, s, op)
                op.insert(0, vertex)

        





# total_courses = 5
# pre_requisites = [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4], [3, 4]]
# print(TopologicalSort().topoSort(pre_requisites, total_courses))