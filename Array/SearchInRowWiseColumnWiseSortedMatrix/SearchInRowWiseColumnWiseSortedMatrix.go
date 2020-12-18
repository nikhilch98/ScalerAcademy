/**
 * @input A : 2D integer array 
 * @input B : Integer
 * 
 * @Output Integer
 */

 func binarySearch(row []int , B int) (int) {
    l,r:=0,len(row)-1
    for l<=r {
        mid := (l+r)/2
        if row[mid] == B {
            return mid
        } else if row[mid] > B {
            r=mid-1
        } else {
            l=mid+1
        }
    }
    return -1
}
func solve(A [][]int , B int )  (int) {
    for i,row := range A {
        j := binarySearch(row,B)
        if j != -1 {
            return (i+1)*1009 + (j+1)
        }
    }
    return -1
}
