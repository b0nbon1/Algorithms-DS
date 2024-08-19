package arrays

import "testing"

func TestArray(t *testing.T) {
	t.Run("Initialize the Array", func(t *testing.T) {
		arr := NewArray()
		if arr.Length() != 0 {
			t.Errorf("Expected length of 0, but got %d", arr.Length())
		}

		if arr.Capacity() != 1 {
			t.Errorf("Expected capacity of 1, but got %d", arr.Capacity())
		}
	})


	t.Run("Append to the Array", func(t *testing.T) {
		arr := NewArray()
		arr.Append(1)
		if arr.Length() != 1 {
			t.Errorf("Expected length of 1, but got %d", arr.Length())
		}
		if arr.Capacity() != 1 {
			t.Errorf("Expected capacity of 1, but got %d", arr.Capacity())
		}

		for i := 0; i < 10; i++ {
			arr.Append(i)
		}

		if arr.Capacity() != 16 {
			t.Errorf("Expected capacity of 4, but got %d", arr.Capacity())
		}
	})

	t.Run("Get from the Array", func(t *testing.T) {
		arr := NewArray()
		for i := 0; i < 5; i++ {
			arr.Append(i+1)
		}
		if arr.Get(0) != 1 {
			t.Errorf("Expected value of 1 at index 0, but got %d", arr.Get(0))
		}
		if arr.Get(1) != 2 {
			t.Errorf("Expected value of 2 at index 1, but got %d", arr.Get(1))
		}
		if arr.Get(2) != 3 {
			t.Errorf("Expected value of 3 at index 2, but got %d", arr.Get(2))
		}
	})

	t.Run("Delete from the Array", func(t *testing.T) {
		arr := NewArray()
		for i := 0; i < 5; i++ {
			arr.Append(i+1)
		}
		arr.Delete(1)
		if arr.Length() != 4 {
			t.Errorf("Expected length of 2, but got %d", arr.Length())
		}
		if arr.Capacity() != 8 {
			t.Errorf("Expected capacity of 4, but got %d", arr.Capacity())
		}
		if arr.Get(0) != 1 {
			t.Errorf("Expected value of 1 at index 0, but got %d", arr.Get(0))
		}
		if arr.Get(1) != 3 {
			t.Errorf("Expected value of 3 at index 1, but got %d", arr.Get(1))
		}
	})
}