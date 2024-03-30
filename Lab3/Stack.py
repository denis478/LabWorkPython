from abc import ABC, abstractmethod
import unittest
class StackInterface(ABC):
    @abstractmethod
    def push(self, item):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass

class Stack(StackInterface):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from an empty stack")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class TestStack(unittest.TestCase):
    def test_push_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_peek(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek(), 2)

    def test_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 2)

if __name__ == '__main__':
    unittest.main()

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Размер стека:", stack.size())
print("Проверка на пустоту?", stack.is_empty())
print("Максимальный элемент:", stack.peek())

while not stack.is_empty():
    print("Извлечение элемента:", stack.pop())