import random
# class QuickSort:
#     def sort(self, A, p, r): 
#         A[:] = self.partition(A, p, r)
#         print(A)
#     def partition(self, A, p, r):
#         def quick(A):
#             if len(A) < 2:
#                 return A #base case
#             else:
#                 temp = A.index(random.choice(A))
#                 A[-1],A[temp] = A[temp],A[-1]
#                 pivot = A[-1]
#                 less = [i for i in A[:-1] if i <= pivot] 
#                 more = [i for i in A[:-1] if i > pivot]
#                 return  quick(less) + [pivot] + quick(more)
                
#         return quick(A)
            
# A = [4,6,7,2,3,1,5]
# QuickSort().sort(A,0,len(A)-1)
        
### IMP if autograder takes len of array -1 make a helper function
import random
class QuickSort:
    def sort(self,A,p,r):
        return self.helper(A,p,r-1)
    def helper(self,A,p,r):
        if p>=r:
            return
        pivotIndex = self.partition(A,p,r)        
        self.helper(A,p,pivotIndex-1)
        self.helper(A,pivotIndex+1,r)

    def partition(self,A,p,r):
        
        i = p-1
        temp = random.randrange(p,r)
        A[r],A[temp]=A[temp],A[r]
        pivot = A[r]
        for j in range(p,r):
            if A[j]<=pivot:
                i+=1
                A[i],A[j]=A[j],A[i]
        A[i+1],A[r]=A[r],A[i+1]
        return i+1


A = [5, 4 ,10, 3, 2, 1]
print(QuickSort().sort(A,0,len(A)))
print(A)

# [3,7,5,2,1,4]
# [3,2,5,7,1,4
# [3,2,1,7,5,4]