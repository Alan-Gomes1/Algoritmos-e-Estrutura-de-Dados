from linked_list import Node


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        """Insere um elemento no topo da pilha"""
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """Remove o elemento do topo da lista"""
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError("The stack is empty")

    def peek(self):
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        stack_data = ""
        ptr = self.top
        while (ptr):
            stack_data += str(ptr.data) + "\n"
            ptr = ptr.next
        return stack_data

    def __str__(self):
        return self.__repr__()
