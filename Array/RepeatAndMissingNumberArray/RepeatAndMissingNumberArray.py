class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    # Time Complexity  : O(n)
    # Space Complexity : O(1)
    def repeatedNumber(self, A):
        n = len(A)
        total_arr = sum(A)
        total_n = (n*(n+1))//2
        total_arr_sq = sum([i*i for i in A])
        total_n_sq = (n*(n+1)*(2*n+1))//6
        
        diff_num = total_n - total_arr
        diff_num_sq = total_n_sq - total_arr_sq
        add_num = diff_num_sq // diff_num
        return [(add_num - diff_num)//2,(add_num + diff_num)//2]
        
        
