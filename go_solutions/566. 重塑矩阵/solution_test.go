package solution

import (
	"reflect"
	"testing"
)

func Test_matrixReshape(t *testing.T) {
	type args struct {
		mat [][]int
		r   int
		c   int
	}

	tests := []struct {
		name string
		args args
		want [][]int
	}{
		{"1", args{[][]int{[]int{1, 2}, []int{3, 4}}, 1, 4}, [][]int{[]int{1, 2, 3, 4}}},
		{"2", args{[][]int{[]int{1, 2}, []int{3, 4}}, 2, 4}, [][]int{[]int{1, 2}, []int{3, 4}}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := matrixReshape(tt.args.mat, tt.args.r, tt.args.c); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("matrixReshape() = %v, want %v", got, tt.want)
			}
		})
	}
}
