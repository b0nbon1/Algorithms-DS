package problems_test

import (
	p "dope-stuff/algos/150-problems"
	"testing"
)

func TestIsAnagram(t *testing.T) {
	t.Run("Is Anagram", func(t *testing.T) {
		s := "racecar"
		tString := "carrace"
		if !p.Is_anagram(s, tString) {
			t.Errorf("Expected to be anagram, but got %t", p.Is_anagram(s, tString))
		}
	})

	t.Run("Does not match character length", func(t *testing.T) {
		s := "raceca"
		tString := "carrace"
		if p.Is_anagram(s, tString) {
			t.Errorf("Expected duplicate integer, but got %t", p.Is_anagram(s, tString))
		}
	})

	t.Run("Does not match character anagrams", func(t *testing.T) {
		s := "racecai"
		tString := "carrace"
		if p.Is_anagram(s, tString) {
			t.Errorf("Expected duplicate integer, but got %t", p.Is_anagram(s, tString))
		}
	})
}
