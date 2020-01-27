package main

type NumArray struct {
	Sum []int
}


func Constructor(nums []int) NumArray {
	var numArray = NumArray{Sum: make([]int, len(nums)+1)}
	for i:=0; i<len(nums); i++ {
		numArray.Sum[i+1] = numArray.Sum[i] + nums[i]
	}
	return numArray
}


func (this *NumArray) SumRange(i int, j int) int {
	return this.Sum[j+1] - this.Sum[i]
}

/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * param_1 := obj.SumRange(i,j);
 */
