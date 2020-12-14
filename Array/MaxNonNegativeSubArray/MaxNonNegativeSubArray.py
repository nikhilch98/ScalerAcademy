class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        res = -1
        l = 0
        r=0
        temp_sum = -1
        temp_l = -1
        temp_r = -1
        for i,val in enumerate(A):
            if val < 0 or temp_sum < 0:
                temp_sum=val
                temp_l = i
                temp_r = i
            else :
                temp_sum+=val
                temp_r+=1
            if (temp_sum > res) or (temp_sum == res and (temp_r-temp_l>r-l)):
                l = temp_l
                r = temp_r
                res = temp_sum
        if res < 0:
            return []
        return A[l:r+1]