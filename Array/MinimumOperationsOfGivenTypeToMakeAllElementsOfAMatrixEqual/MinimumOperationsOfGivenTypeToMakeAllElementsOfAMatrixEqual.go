/**
 * @input A : 2D integer array 
 * @input B : Integer
 * 
 * @Output Integer
 */
 import "sort"
 func abs(a int) (int) {
	 if a < 0 {
		 return -1 * a
	 }
	 return a
 }
 func solve(A [][]int , B int )  (int) {
	 arr := make([]int,0)
	 for _,row := range A {
		 arr = append(arr,row...)
	 }
	 sort.Slice(arr, func(i,j int) bool {
			 return arr[i] < arr[j]
	 })
	 res := 0
	 res_val := arr[len(arr)/2]
	 for _,row := range A {
		 for _,val := range row {
			 if abs(val-res_val)%B!=0 {
				 return -1
			 }
			 res +=abs(val-res_val)/B
		 }
	 }
	 return res
 }
 