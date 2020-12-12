class Solution:
	# @param A : tuple of integers
	# @return an integer
    
    ############################ Solution 1 (Using Precomputed Suffix and Prefix Array) ####################
    # Time Complexity  : O(n)
    # Space Complexity : O(n)
    # Solution : Maintain a left max and right max for each element. 
    # Water level stored at each element is the min of left max and right max minus the element height
	def trap_1(self, A):
        l_max=[0]*len(A)
        r_max=[0]*len(A)
        for i in range(len(A)-1,-1,-1):
            if i != len(A)-1:
                r_max[i]=max(r_max[i+1],A[i+1])
        for i in range(len(A)):
            if i != 0:
                l_max[i]=max(l_max[i-1],A[i-1])
        res = 0
        for i in range(len(A)):
            res+=max(0,min(r_max[i],l_max[i])-A[i])
        return res


    
    ############################ Solution 2 (Using 2 pass divide and conquer solution)####################
    # Time Complexity  : O(n)
    # Space Complexity : O(1)
    # Solution : Find the max_val and its index. Divide the array into two parts.
    # For the left part of the array - right max is max_val
    # For the right part of the array - left max is max_val
	def trap_2(self, A):
        max_val = A[0]
        max_ind = 0
        for ind,val in enumerate(A):
            if val > max_val:
                max_val = val
                max_ind = ind
        res = 0
        l_max = 0
        for i in range(max_ind):
            res+=max(0,min(l_max,max_val)-A[i])
            l_max = max(l_max,A[i])
        r_max = 0
        for i in range(len(A)-1,max_ind,-1):
            res+=max(0,min(r_max,max_val)-A[i])
            r_max = max(r_max,A[i])
        return res


    ############################ Solution 3 (2 pointer approach)####################
    # Time Complexity  : O(n)
    # Space Complexity : O(1)
    #
    # Solution : Take two pointers l as 0 and r as len(A) - 1 . We then have 2 conditions
    # If left_max <= right max : 
    #       1) Then take element A[l].
    #       2) Left max of element A[l] is l_max 
    #       3) Right max of element A[l] is always >= current r_max
    #       4) Therefore min(l_max,r_max) of A[l] is alwasy l_max
    #       5) Increment l
    #
    # If left_max > right max : 
    #       1) Then take element A[r].
    #       2) Right max of element A[r] is r_max 
    #       3) Left max of element A[r] is always >= current l_max
    #       4) Therefore min(l_max,r_max) of A[r] is alwasy r_max
    #       5) Decrement r
	def trap_3(self, A):
        l_max,r_max,l,r,res=0,0,0,len(A)-1,0
        while (l<=r):
            if r_max <= l_max:
                res+= max(0,r_max-A[r])
                r_max = max(r_max,A[r])
                r-=1
            else :
                res+= max(0,l_max-A[l])
                l_max = max(l_max,A[l])
                l+=1
        return res
            
            
            