package problems

func Is_anagram(s, t string) bool {
	if len(s) != len(t) {
		return false
	}
	checkMap := make(map[string]int)

	for i := range s {
		sc := string(s[i])
		checkMap[sc] += 1
		tc := string(t[i])
		checkMap[tc] -= 1
	}

	for _,v := range checkMap {
		if v != 0 {
			return false
		}
	}

	return true
}
