class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def add(self, data):
        if self.head:
            ptr = self.head
            while (ptr.next):
                ptr = ptr.next
            ptr.next = Node(data)
        else:
            self.head = Node(data)
        self._size += 1
        return

    def __len__(self):
        return self._size

    def _getnode(self, index):
        ptr = self.head
        for _ in range(index):
            if ptr:
                ptr = ptr.next
            else:
                raise IndexError("list index out of range")
        return ptr

    def __getitem__(self, index):
        ptr = self._getnode(index)
        if ptr:
            return ptr.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, data):
        ptr = self._getnode(index)
        if ptr:
            ptr.data = data
        else:
            raise IndexError("list index out of range")

    def index(self, data):
        ptr = self.head
        i = 0
        while (ptr):
            if ptr.data == data:
                return i
            ptr = ptr.next
            i += 1
        raise ValueError(f"{data} is not in list")

    def insert(self, index, data):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            ptr = self._getnode(index-1)
            node.next = ptr.next
            ptr.next = node
        self._size += 1

    def remove(self, data):
        if self.head == None:
            raise ValueError(f"{data} is not in list")
        elif self.head == data:
            self.head = self.head.next
            self._size -= 1
        else:
            ancestor = self.head
            ptr = self.head.next
            while (ptr):
                if ptr.data == data:
                    ancestor.next = ptr.next
                    ptr.next = None
                    self._size -= 1
                ancestor = ptr
                ptr = ptr.next
            return True
        raise ValueError(f"{data} is not in list")

    def __repr__(self):
        list_data = ""
        ptr = self.head
        while (ptr):
            list_data += str(ptr.data) + " "
            ptr = ptr.next
        return list_data

    def __str__(self):
        return self.__repr__()
