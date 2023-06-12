from maxHeap import MaxHeap

mh = MaxHeap()

print(mh.top())  # None

mh.add(10)
print(mh.top())
mh.print_maxheap()

mh.add(20)
print(mh.top())
mh.print_maxheap()

mh.add(5)
print(mh.top())
mh.print_maxheap()

mh.add(3)
print(mh.top())
mh.print_maxheap()

mh.add(30)
print(mh.top())
mh.print_maxheap()

mh.pop()
print(mh.top())
mh.print_maxheap()

mh.pop()
print(mh.top())
mh.print_maxheap()

mh.pop()
mh.pop()
print(mh.top())
mh.print_maxheap()

mh.pop()
print(mh.top())
mh.print_maxheap()

'''
None
10
[10]
20
[20, 10]
20
[20, 10, 5]
20
[20, 10, 5, 3]
30
[30, 20, 5, 3, 10]
20
[20, 10, 5, 3]
10
[10, 3, 5]
3
[3]
None
[]
'''