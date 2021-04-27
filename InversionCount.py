# class InversionCount:
#     def count(self, A: [int]) -> [int]:
#         og_A = list(A)
#         self.sort(A,0,len(A)-1)
#         final = []
#         while A!=[]:
#             B_index = self.search(A,og_A[0])
#             final.append(B_index)
#             og_A = og_A[1:]
#             A.pop(B_index)
#         return final
#     #############Binary Search#########################
#     def search(self,A,key):
#             def _binary_search(key, first, end, A):
#                 try:
#                     if end < first:
#                         return -1
#                     mid = (first + end) // 2
#                     if A[mid] == key:
#                         return mid
#                     if A[mid] > key:
#                         return _binary_search(key, first, mid-1, A)
#                     else:
#                         return _binary_search(key, mid+1, end, A)
#                 except:
#                     return -1
#             return _binary_search(key, 0, len(A), A)

#     #############Merge Sort#############
#     def sort(self, A, p, r):
#         if p>=r:
#             return 
#         mid = (p+r)//2
#         #print(A[p:mid+1],A[mid+1:r+1],p,mid,r)
#         self.sort(A,p,mid)
#         # print(A[p:q],A[q:r],p,q,r)
#         self.sort(A,mid+1,r)
#         # print(A[p:q],A[q:r],p,q,r)
#         self.merge(A,p,mid,r)


    
#     def merge(self, A, p, q, r): 
#         left  = A[p:q+1]
#         right  = A[q+1:r+1]
#         i, j = 0, 0
#         temp_p = p
#         while i<len(left) and j<len(right):
#             if left[i]<right[j]:
#                 A[temp_p]=left[i]
#                 i+=1
#                 temp_p+=1
#             else:
#                 A[temp_p] = right[j]
#                 j += 1
#                 temp_p += 1
        
#         while i<len(left):
#             A[temp_p] = left[i]
#             i+=1
#             temp_p+=1
        
#         while j<len(right):
#             A[temp_p] = right[j]
#             j+=1
#             temp_p+=1


        

        
# print(InversionCount().count([5,4,7,9,2]))







class InversionCount:
    def count(self, A: [int]) -> [int]:
        index = list(range(len(A)))  # initialize from 0 to len(A) 
        result = [0]*len(A) # initialize with zeros for all elements 

        self.sort(A,0,len(A)-1, index, result)
        return result
    def sort(self, A, p, r, index, result):
            if p>=r:
                return 
            mid = (p+r)//2
            #print(A[p:mid+1],A[mid+1:r+1],p,mid,r)
            self.sort(A,p,mid, index, result)
            # print(A[p:q],A[q:r],p,q,r)
            self.sort(A,mid+1,r, index, result)
            # print(A[p:q],A[q:r],p,q,r)
            self.merge(A,p,mid,r, index, result)


        
    def merge(self, A, p, q, r, index, result): 
        left  = index[p:q+1]
        right  = index[q+1:r+1]
        i, j = 0, 0
        temp_p = p
        count = 0

        while i<len(left) and j<len(right):
            if A[left[i]]>A[right[j]]:
                count += 1
                index[temp_p]=right[j]
                j+=1
                temp_p+=1
            else:
                result[left[i]] = result[left[i]] + count
                index[temp_p] = left[i]
                i += 1
                temp_p += 1
        
        while i<len(left):
            result[left[i]] = result[left[i]] + count
            index[temp_p] = left[i]
            i+=1
            temp_p+=1
        
        while j<len(right):
            index[temp_p] = right[j]
            j+=1
            temp_p+=1

print(InversionCount().count([5,4,3,2,1]))