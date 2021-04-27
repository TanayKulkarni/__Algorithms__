class SeamCarving:
    def carve_seam(self, disruption: [[int]]) -> [int]:
        # print(disruption)
        l = len(disruption)
        for i in range(1,len(disruption)):
            for j in range(l):
                if j==0:
                    disruption[i][j]  += min(disruption[i-1][j],disruption[i-1][j+1])
                elif j==l-1:
                    disruption[i][j]  += min(disruption[i-1][j],disruption[i-1][j-1])
                else:
                    disruption[i][j]  += min(disruption[i-1][j-1],disruption[i-1][j],disruption[i-1][j+1])

        row = len(disruption)
        result = [0]*row
        result[row-1] = disruption[row-1].index(min(disruption[row-1]))
        # i = len(disruption)-2
        for i in range(row-2,-1,-1):
            j = result[i+1]
            if j==0:
                temp = disruption[i][j:j+2]
                ind = temp.index(min(temp))
                result[i] = ind+j
            elif j==l-1:
                temp = disruption[i][j-1:j+1]
                ind = temp.index(min(temp))
                result[i] =ind+j-1
            else:
                temp = disruption[i][j-1:j+2]
                ind = temp.index(min(temp))
                result[i]=ind+j-1
        return result
# print(SeamCarving().carve_seam([[1, 2, 0, 3], [1, 4, 4, 4], [1, 2, 3, 4], [3, 1, 1, 3]]))

# print(SeamCarving().carve_seam([[3, 2, 2, 3, 1, 2], [2, 1, 3, 2 ,3, 1], [3,4,3,1,3,1], [3,2,1,2,4,3],[1,3,3,2,4,3]]))





