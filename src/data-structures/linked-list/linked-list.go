package linkedlist

type  Node struct {
	Value int
	Next *Node
}

type LinkedList struct {
	Head *Node
}

func (list *LinkedList) Append(data int) {
	newNode := &Node{Value: data}

    if list.Head == nil {
        list.Head = newNode
    } else {
        current := list.Head
        for current.Next != nil {
            current = current.Next
        }
        current.Next = newNode
    }
}

func (list *LinkedList) Prepend(data int) {
	newNode := &Node{Value: data}

	if list.Head == nil {
		list.Head = newNode
	} else {
		curr := list.Head
		list.Head = newNode
		list.Head.Next = curr
	}
}

func (list *LinkedList) Peek() int {
	return list.Head.Value
}

func (list *LinkedList) Pop() int {
	if list.Head == nil {
		return list.Head.Value
	}
	curr := list.Head;
	for curr.Next != nil {
		curr = curr.Next
	}
	return curr.Value
}

func (list *LinkedList) Remove(data int) {
	if list.Head == nil {
		return
	}
	if list.Head.Value == data {
		list.Head = list.Head.Next
		return
	}
	curr := list.Head
	for curr.Next != nil {
		if curr.Next.Value == data {
			curr.Next = curr.Next.Next
			return
		}
		curr = curr.Next
	}
}
