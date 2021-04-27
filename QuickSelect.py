

import random
class QuickSelect:
    def select(self,A,k):
        p = 0
        r = len(A)-1
        return self.helper(A,p,r,k)
        
    def helper(self,A,p,r,k):
        pivotIndex = self.partition(A,p,r)
        if pivotIndex==k:
            return A[k]
        elif pivotIndex < k:
            return self.helper(A,pivotIndex+1,r,k)
        else:
            return self.helper(A,p,pivotIndex-1,k)

    def partition(self,A,p,r):
        
        i = p-1
        # temp = random.randint(p,r)
        # A[r],A[temp]=A[temp],A[r]
        # l = list(A[p:r+1])
        y = A.index(self.median_of_median(A[p:r+1]))
        pivot_Index = y  #Call median of median function to get the pivot Element
        A[r],A[pivot_Index]=A[pivot_Index],A[r]
        pivot = A[r]
        for j in range(p,r):
            if A[j]<=pivot:
                i+=1
                A[i],A[j]=A[j],A[i]
        A[i+1],A[r]=A[r],A[i+1]
        return i+1
    
    def median_of_median(self,e):
        n = 5
        median = []
        ind = []
        for i in range(0,len(e),5):
            
            # temp = list(sorted(e[i:i+n]))
            temp = e[i:i+n]
            temp.sort()
            # temp = self.sort(A,i:i+n)
            mid = temp[len(temp)//2]    
            median.append(mid)
        median.sort()
        mid = median[len(median)//2]        
        return mid

    

A = [1, 3, 5, 6, 7, 8]
print(QuickSelect().select(A,3))
