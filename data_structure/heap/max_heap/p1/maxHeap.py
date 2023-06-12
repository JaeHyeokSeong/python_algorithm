class MaxHeap:
    def __init__(self, numbers=None):
        self.nodes = [0]
        if numbers is not None:
            for number in numbers:
                self.add(number)

    def add(self, number):
        self.nodes.append(number)
        current_index = len(self.nodes) - 1

        while current_index > 1:
            parent_index = current_index // 2
            if self.nodes[current_index] <= self.nodes[parent_index]:
                break
            else:
                self.nodes[current_index], self.nodes[parent_index] = self.nodes[parent_index], \
                    self.nodes[current_index]
                current_index = parent_index

    def pop(self):
        if len(self.nodes) > 1:
            self.nodes[1], self.nodes[len(self.nodes) - 1] = self.nodes[len(self.nodes) - 1], self.nodes[1]
            self.nodes.pop()

            current_index = 1
            child_index = 2

            while child_index <= len(self.nodes) - 1:
                if child_index < len(self.nodes) - 1 and self.nodes[child_index] < self.nodes[child_index + 1]:
                    child_index += 1
                if self.nodes[current_index] >= self.nodes[child_index]:
                    break
                else:
                    self.nodes[current_index], self.nodes[child_index] = self.nodes[child_index], \
                        self.nodes[current_index]
                    current_index = child_index
                    child_index = current_index * 2

    def top(self):
        if len(self.nodes) <= 1:
            return None
        return self.nodes[1]

    def print_maxheap(self):
        if len(self.nodes) == 1:
            print("[]")
        else:
            print(self.nodes[1:])

