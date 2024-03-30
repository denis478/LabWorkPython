from abc import ABC, abstractmethod

class AbstractArray(ABC):
    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def set(self, index, value):
        pass

    @abstractmethod
    def length(self):
        pass
class Array(AbstractArray):
    def __init__(self, size):
        self.data = [None] * size

    def get(self, index):
        return self.data[index]

    def set(self, index, value):
        self.data[index] = value

    def length(self):
        return len(self.data)

import unittest

class TestArray(unittest.TestCase):
    def test_get_set(self):
        arr = Array(5)
        arr.set(0, 1)
        arr.set(1, 2)
        self.assertEqual(arr.get(0), 1)
        self.assertEqual(arr.get(1), 2)

    def test_length(self):
        arr = Array(3)
        self.assertEqual(arr.length(), 3)

if __name__ == '__main__':
    unittest.main()

array = Array(5)
array.set(0, 10)
array.set(1, 20)
print("Длина массива:", array.length())
print("Элемент с индексом 0:", array.get(0))
print("Элемент с индексом 1:", array.get(1))