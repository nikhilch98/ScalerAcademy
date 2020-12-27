/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
 import "sort"
 func wave(A []int )  ([]int) {
	 sort.Slice(A, func(i, j int) bool {  
		 return A[i] < A[j] 
	 }) 
	 for i:=1;i<len(A);i+=2{
		 A[i],A[i-1]=A[i-1],A[i]
	 }
	 return A
 }
 