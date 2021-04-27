class Scheduling:
    

    def schedule(self, A : [[int]]) -> int:
        
        A.sort(key=lambda x: x[1])
        first = 9000000
        second = -9000000
        cnt = 0
        flag = True

        for i in range(0,len(A)):
            new_first,new_second = A[i][0],A[i][1]
            if new_first<new_second:
                if new_first>=second:
                    cnt+=1
                    first = new_first
                    second = new_second
            elif flag:
                first = new_first
                second = new_second
                flag=False

        for i in range(0,len(A)):
            new_first,new_second = A[i][0],A[i][1]
            if new_first>new_second:
                if new_first>=second:
                    cnt+=1
                    break
        return cnt












        
       
# A = [[64800,21600], [75600,14400], [10800,50400], [46800, 68400]]
# A = [[100, 86000], [86000, 100]]
# A= [[0,3],[0,6],[8,11],[0,17],[19,23]]


# print(Scheduling().schedule(A))
