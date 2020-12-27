class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        r_min = [A[-1]]*len(A)
        for i in range(len(A)-2,-1,-1):
            r_min[i]=min(r_min[i+1],A[i+1])
        l_max=A[0]
        res = 0
        for i in range(len(A)):
            l_max=max(l_max,A[i])
            if i == len(A)-1 or l_max <= r_min[i]:
                res+=1
        return res