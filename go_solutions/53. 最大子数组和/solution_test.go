package solution

import "testing"

type args struct {
	nums []int
}

var tests = []struct {
	name string
	args args
	want int
}{
	{"1", args{[]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}}, 6},
	{"2", args{[]int{1}}, 1},
	{"2", args{[]int{5, 4, -1, 7, 8}}, 23},
}

func Test_maxSubArray(t *testing.T) {
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxSubArray(tt.args.nums); got != tt.want {
				t.Errorf("maxSubArray() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_maxSubArray1(t *testing.T) {
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxSubArray1(tt.args.nums); got != tt.want {
				t.Errorf("maxSubArray1() = %v, want %v", got, tt.want)
			}
		})
	}
}
