#Функция принимает n, возвращает список из чисел Фибоначчи
def fibonacci(n):
    a1 = 1
    a2 = 1
    N = int(n)
    M = [1, 1]

    for i in range (2, N):
        a1, a2 = a2, a1 + a2
        M.append(a2)

    print(M)
    return M

#Функция принимает список чисел, возвращает его отсортированную копию(Сортировка пузырьком)
def sorting(n):
    print("сортировка")

    a = [1, 4, 3, 2, 5, 9, 7, 8, 6]

    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)
    return(a)
#функция принимает 3 аргумента: число 1, число 2 и знак действия: +, -, *, / выполняет действие и возвращает результат (Калькулятор)
def calculator(x,y,z):
    Z = z
    if Z in ('+', '-', '*', '/'):
        X = x
        Y = y
        if Z == '+':
            return(X + Y)
        elif Z == '-':
            return(X - Y)
        elif Z == '*':
            return(X * Y)
        elif Z == '/':
            if Y != 0:
                return(X / Y)
            else:
                return("Деление на ноль!")
    else:
        return("Неверный знак операции!")
