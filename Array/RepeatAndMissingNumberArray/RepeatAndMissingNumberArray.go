/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
 func repeatedNumber(A []int )  ([]int) {
    n := len(A)
    total_arr,total_arr_sq := 0,0
    total_n := (n*(n+1))/2
    total_n_sq := (n*(n+1)*(2*n+1))/6
    for _,val := range A {
        total_arr+=val
        total_arr_sq+=val*val
    }
    diff_num := total_n - total_arr
    diff_num_sq := total_n_sq - total_arr_sq
    add_num := diff_num_sq / diff_num
    return []int{(add_num - diff_num)/2,(add_num + diff_num)/2}
}
