from linkedList import LinkedList

ll = LinkedList()

ll.push_front(10)
ll.push_front(20)
ll.push_front(30)
ll.push_front(40)

ll.front()
ll.print_linkedlist()

ll.pop_front()
ll.pop_front()

ll.front()
ll.print_linkedlist()

ll.pop_front()
ll.pop_front()
ll.front()
ll.print_linkedlist()

print(f"size: {ll.size}")

ll.push_back(10)
ll.print_linkedlist()

ll.push_at(20, 0)
ll.print_linkedlist()

ll.push_at(30, 1)
ll.print_linkedlist()

ll.push_at(40, 1)
ll.print_linkedlist()

ll.push_at(50, 3)
ll.print_linkedlist()

print(f'size: {ll.size}')
