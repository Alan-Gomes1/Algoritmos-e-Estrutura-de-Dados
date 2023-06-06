from linked_list import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node
        self._size += 1

    def pop(self):
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem
        raise IndexError("The queue is empty")

    def peek(self):
        if self._size > 0:
            return self.first.data
        raise IndexError("The queue is empty")

    def __len__(self):
        return self._size

    def __repr__(self):
        if self._size > 0:
            representation = ""
            ptr = self.first
            while (ptr):
                representation += f"{ptr.data} "
                ptr = ptr.next
            return representation
        raise IndexError("Empty queue")


a = Queue()
a.push(5)
a.push(1)
a.push(7)
print(a)
print(a.pop())
print(a)
print(a.peek())
