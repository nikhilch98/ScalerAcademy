/**
 * @input A : Integer array
 * 
 * @Output Integer array.
 */
 func maxset(A []int )  ([]int) {
    res := -1
    l := 0
    r:=0
    temp_sum := -1
    temp_l := -1
    temp_r := -1
    for i,val := range A {
        if val < 0 || temp_sum < 0 {
            temp_sum=val
            temp_l = i
            temp_r = i
        } else {
            temp_sum+=val
            temp_r+=1
        }
        if (temp_sum > res) || (temp_sum == res && (temp_r-temp_l>r-l)){
            l = temp_l
            r = temp_r
            res = temp_sum
        }
    }
    if res < 0{
        return []int{}
    }
    return A[l:r+1]
}