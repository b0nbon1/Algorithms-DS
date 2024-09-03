package problems

func TwoSum(nums []int, target int) []int {
    diffMap := make(map[int]int)

    for i, v := range nums {
		val, ok := diffMap[target - v]
		if ok {
			return []int{i, val}
		}
		diffMap[v] = i
	}

	return []int{-1, -1}
}