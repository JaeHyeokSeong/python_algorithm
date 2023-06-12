# min heap
from minHeap import MinHeap

numbers = [3, 4, 1, -2]
mh = MinHeap(numbers)

print(mh.top())  # -2
mh.print_minheap()

mh.pop()
print(mh.top())  # 1
mh.print_minheap()

mh.pop()
print(mh.top())  # 3
mh.print_minheap()

mh.add(-1)
print(mh.top())  # -1
mh.print_minheap()

mh.pop()
print(mh.top())  # 3
mh.print_minheap()
