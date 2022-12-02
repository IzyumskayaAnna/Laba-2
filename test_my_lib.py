import my_lib
import pytest


# Тест функции, находящей простые числа, меньше заданного n
class TestFindPrimes:
#Тест функции Фибоначи с корректными данными. Функция возвращает массив чисел Фибоначи.
    def test_on_correct_fibonacci(self):
        assert my_lib.fibonacci(6) == [1, 1, 2, 3, 5, 8]
#Тест функции Фибоначи с некорректными данными. Функция вызывает исключение ValueError.
    def test_on_incorrect_fibonacci(self):
        with pytest.raises(ValueError):
            assert my_lib.fibonacci('qwerty')

#Тест функции сортировки пузырьком с корректными данными. Функция возвращает массив чисел.
    def test_on_correct_sorting(self):
        assert my_lib.sorting(9) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Тест функции сортировки пузырьком с некорректными данными. Функция вызывает исключение TypeError.
    def test_on_incorrect_sorting(self):
        with pytest.raises(TypeError):
            assert my_lib.sorting('qwetryt')

#Тест функции калькулятор с корректными данными. Функция возвращает число.
    def test_on_correct_calculator(self):
        assert my_lib.calculator(1, 2, '+') == 3
        assert my_lib.calculator(16, 8, '-') == 8
        assert my_lib.calculator(30, 5, '/') == 6
        assert my_lib.calculator(2, 8, '*') == 16
#Тест функции калькулятор с некорректными данными. Функция вызывает исключение TypeError.
    def test_on_incorrect_calculator(self):
        with pytest.raises(TypeError):
            assert my_lib.calculator(1)

