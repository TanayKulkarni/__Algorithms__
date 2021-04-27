
class MakingChange:
    def minimumCoins(self, money, coins):
       
        A = [float('inf')]*(money+1)
        print(money,coins)
        A[0] = 0
        flag = False
        for sikka in coins:
            for i in range(sikka,money+1):
                A[i]=min(A[i],A[i-sikka]+1)
        return A[money] if A[money]!=float('inf') else -1


# print(MakingChange().minimumCoins(75,[50]))
print(MakingChange().minimumCoins(0,[1,2,5,10,25]))