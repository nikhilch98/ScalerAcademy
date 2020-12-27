class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        arr = []
        for val in A:
            arr.extend(val)
        arr.sort()
        res = 0
        res_val = arr[len(arr)//2]
        for row in A:
            for val in row:
                if abs(val-res_val)%B!=0:
                    return -1
                res +=abs(val-res_val)//B
        return res