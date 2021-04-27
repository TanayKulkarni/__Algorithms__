class MajorityElement:
    def majority(self, A):
        d = {}
        for i in A:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m = max(d, key = d.get) #O(n)
        if d[m]>len(A)//2:
            return m
        else:
            return -1 

A = [1, 3, 5, 4, 5, 5, 5, 5]
print(MajorityElement().majority(A))