package main

import "dope-stuff/algos/src/data-structures/arrays"

func main() {
	a := arrays.NewArray()
	a.Append(1)
	print(a.Get(0))
}
