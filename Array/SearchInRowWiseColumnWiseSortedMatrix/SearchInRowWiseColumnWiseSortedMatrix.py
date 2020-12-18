class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    # Time Complexity : O(nlog(n))
    # Space Complexity : O(1)
    def binary_search(self,row,B):
        l,r=0,len(row)-1
        while(l<=r):
            mid = (l+r)//2
            if row[mid] == B:
                return mid
            elif row[mid] > B:
                r=mid-1
            else :
                l=mid+1
        return -1
    def solve(self, A, B):
        for i,row in enumerate(A):
            j = self.binary_search(row,B)
            if j != -1:
                return (i+1)*1009 +(j+1)
        return -1