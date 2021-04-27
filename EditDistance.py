
                
class EditDistance:
    def editDistance(self, word1, word2):
        p =[[]]
        p[0] = list(range(len(word1)+1))
        for k in range(1,len(word2)+1):
           p.append([k]*(len(word1)+1))


        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word1[j-1]==word2[i-1]:
                    p[i][j]=p[i-1][j-1]
                else:
                    p[i][j] = min(p[i-1][j-1], p[i-1][j] , p[i][j-1] )+1
        return p[-1][-1]
                
# print(EditDistance().editDistance("tgcatat","atccgat"))