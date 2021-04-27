class HeapSort:
    
    def heapify(self, A, n, i):
        largest = i
        l = 2*i+1
        r = 2*i+2
        if l<=n-1 and A[l]>A[i]:
            largest = l
        if r<=n-1 and A[r]>A[largest]:
            largest = r
        if largest!=i:
            A[i],A[largest]=A[largest],A[i]
            self.heapify(A, n, largest)

    def heapSort(self, A):
        # print(A)
        n = len(A)
        for i in range(n//2-1,-1,-1):
             self.heapify(A,n,i)
        for i in range(n-1, 0, -1):
            A[i], A[0] =A[0], A[i]  # swap
            self.heapify(A, i, 0)
        
        # print(A)
        return A

print(HeapSort().heapSort([10,20,15,12,40,25,18]))