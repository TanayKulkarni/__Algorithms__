class BinarySearch:
    def search(self,A,key):
        def _binary_search(key, first, end, A):
            try:
                if end < first:
                    return -1
                mid = (first + end) // 2
                if A[mid] == key:
                    return mid
                if A[mid] > key:
                    return _binary_search(key, first, mid-1, A)
                else:
                    return _binary_search(key, mid+1, end, A)
            except:
                return -1
        return _binary_search(key, 0, len(A), A)


