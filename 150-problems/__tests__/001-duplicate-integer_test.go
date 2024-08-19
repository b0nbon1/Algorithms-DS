package problems_test

import (
	p "dope-stuff/algos/150-problems"
	"testing"
)

func TestHasDuplicate(t *testing.T) {
	t.Run("Has Duplicate integer", func(t *testing.T) {
		nums := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 1}
		if !p.Duplicate_integer(nums) {
			t.Errorf("Expected duplicate integer, but got %t", p.Duplicate_integer(nums))
		}
	})

	t.Run("Does not contain Duplicate integer", func(t *testing.T) {
		nums := []int{1, 2, 3, 4, 5}
		if p.Duplicate_integer(nums) {
			t.Errorf("Expected duplicate integer, but got %t", p.Duplicate_integer(nums))
		}
	})
}