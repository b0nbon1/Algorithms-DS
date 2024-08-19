package arrays

// Array is a struct that represents an array
type array struct {
	len        int
	capacity   int
	data       []int
}

// NewArray creates a new array
func NewArray() *array {
	return &array{
		len:      0,
		capacity: 1,
		data:     make([]int, 1),
	}
}

// Append adds a value to the array
func (a *array) Append(value int) {
	if a.len == a.capacity {
		a.resize()
	}
	a.data[a.len] = value
	a.len++
}

// resize resizes the array
func (a *array) resize() {
	a.capacity *= 2
	newData := make([]int, a.capacity)
	for i := 0; i < a.len; i++ {
		newData[i] = a.data[i]
	}
	a.data = newData
}

// Get gets a value from the array
func (a *array) Get(index int) int {
	if index < 0 || index >= a.len {
		return -1
	}
	return a.data[index]
}

// Delete deletes a value from the array
func (a *array) Delete(index int) {
	if index < 0 || index >= a.len {
		return
	}
	for i := index; i < a.len-1; i++ {
		a.data[i] = a.data[i+1]
	}
	a.len--
}

// Length returns the length of the array
func (a *array) Length() int {
	return a.len
}

// Capacity returns the capacity of the array
func (a *array) Capacity() int {
	return a.capacity
}

// Data returns the data of the array
func (a *array) Data() []int {
	return a.data
}

// Set sets a value in the array
func (a *array) Set(index, value int) {
	if index < 0 || index >= a.len {
		return
	}
	a.data[index] = value
}