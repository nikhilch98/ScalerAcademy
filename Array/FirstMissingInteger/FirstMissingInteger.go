/**
 * @input A : Integer array
 * 
 * @Output Integer
 */

 func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func firstMissingPositive(A []int )  (int) {
    least_negative_index := 0
    for ind,val := range A {
        if val > 0 {
            A[least_negative_index],A[ind]=A[ind],A[least_negative_index]
            least_negative_index++
        }
    }
    for i:=0;i<least_negative_index;i++ {
        mark_ind := abs(A[i])-1
        if mark_ind < least_negative_index {
            A[mark_ind] = -1 * abs(A[mark_ind])
        }
    }
    for i:=0;i<least_negative_index;i++ {
        if A[i] > 0 {
            return i+1
        }
    }
    return least_negative_index+1
}