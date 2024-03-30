def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

import unittest

class TestShellSort(unittest.TestCase):
    def test_shell_sort(self):
        # Проверяем сортировку списка из чисел
        arr1 = [64, 25, 12, 22, 11]
        print(f'Массив до сортировки{arr1}')
        self.assertEqual(shell_sort(arr1), [11, 12, 22, 25, 64])
        print(f'Массив после сортировки{arr1}')

        # Проверяем сортировку списка из строк
        arr2 = ['apple', 'banana', 'cherry', 'date']
        print(f'Массив до сортировки{arr2}')
        self.assertEqual(shell_sort(arr2), ['apple', 'banana', 'cherry', 'date'])
        print(f'Массив после сортировки{arr2}')


        # Проверяем сортировку списка с повторяющимися элементами
        arr3 = [5, 3, 2, 2, 8, 5, 7]
        print(f'Массив до сортировки{arr3}')
        self.assertEqual(shell_sort(arr3), [2, 2, 3, 5, 5, 7, 8])
        print(f'Массив после сортировки{arr3}')

        # Проверяем сортировку пустого списка
        arr4 = []
        self.assertEqual(shell_sort(arr4), [])
        print(f'Пустой массив{arr4}')

        # Проверяем сортировку списка из одного элемента
        arr5 = [42]
        self.assertEqual(shell_sort(arr5), [42])
        print(f'Массив из одного элемента{arr5}')


if __name__ == '__main__':
    unittest.main()