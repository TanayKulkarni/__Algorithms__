

# class BinarySearch2D:
#     def search(self, M: [[int]], q: int) -> [int, int]:

#         total_elem = len(M) * len(M[0])
#         begin = 0
#         end = total_elem - 1
#         return self.search_bin2d(M, q, begin, end)

#     def search_bin2d(self, M, key, begin, end):

#         if not M or begin > end:
#             return [-1, -1]

#         mid_point = (begin + end) // 2

#         row = mid_point // len(M[0])
#         col = mid_point % len(M[0])

#         mid_element = M[row][col]

#         if key == mid_element:
#             return [row, col]
#         if key < mid_element:
#             end = mid_point - 1
#             return self.search_bin2d(M, key, begin, end)
#         else:
#             begin = mid_point + 1
#             return self.search_bin2d(M, key, begin, end)

# # if ___name__ == "__main__":

# print(BinarySearch2D().search([[0,2,3],[4,5,6],[7,8,9]], 12))


class BinarySearch2D:
    def search(self, M: [[int]], q: int) -> [int, int]:
        if not M:
            return [-1,-1]
        total_elem = len(M) * len(M[0])
        begin = 0
        end = total_elem - 1
        
        while begin<=end:
            mid_point = (begin + end) // 2
            row = mid_point // len(M[0])
            col = mid_point % len(M[0])
            mid_element = M[row][col]
            if q == mid_element:
                return [row,col]
            if q<mid_element:
                end = mid_point-1
            else:
                begin = mid_point+1
        return [-1,-1]







