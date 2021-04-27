class MergeSort:
    def sort(self, A, p, r):
        if p>=r:
            return 
        mid = (p+r)//2
        print(A[p:mid+1],A[mid+1:r+1],p,mid,r)
        self.sort(A,p,mid)
        # print(A[p:q],A[q:r],p,q,r)
        self.sort(A,mid+1,r)
        # print(A[p:q],A[q:r],p,q,r)
        self.merge(A,p,mid,r)


    
    def merge(self, A, p, q, r): 
        left  = A[p:q+1]
        right  = A[q+1:r+1]
        i, j = 0, 0
        temp_p = p
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                A[temp_p]=left[i]
                i+=1
                temp_p+=1
            else:
                A[temp_p] = right[j]
                j += 1
                temp_p += 1
        
        while i<len(left):
            A[temp_p] = left[i]
            i+=1
            temp_p+=1
        
        while j<len(right):
            A[temp_p] = right[j]
            j+=1
            temp_p+=1
        
    
    
    
    
# A = [] 
# MergeSort().sort(A,0,len(A)-1)
# print(A)
    
    
    
    
    
    
    
    
    
    
    
    
