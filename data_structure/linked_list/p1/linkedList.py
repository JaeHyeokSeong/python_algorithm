class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, value):
        new_node = Node(value)
        self.size += 1

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node

    def pop_front(self):
        if self.size < 1:
            return

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.right
            self.head.left = None

        self.size -= 1

    def front(self):
        if self.size >= 1:
            print(self.head.value)
        else:
            print('None')

    def push_back(self, value):
        new_node = Node(value)
        self.size += 1

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node

    def push_at(self, value, index):
        if not (0 <= index < self.size):
            print(f'index {index} is out of index range')
            return

        if index == 0:
            self.push_front(value)
        # elif index == self.size - 1:
        #     self.push_back(value)
        else:
            new_node = Node(value)
            temp = self.head

            for i in range(0, index):
                temp = temp.right

            new_node.left = temp.left
            temp.left = new_node
            new_node.left.right = new_node
            new_node.right = temp
            self.size += 1

    def print_linkedlist(self):
        temp = self.head
        print('values: ', end='')
        while temp:
            print(temp.value, end=' ')
            temp = temp.right
        print()