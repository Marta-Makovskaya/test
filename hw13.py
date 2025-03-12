#Задача 1
def fibonacci_sequence(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
def main():
    try:
        n = int(input("Введите номер числа Фибоначчи, до которого хотите вывести последовательность: "))
        if n < 0:
            print("Пожалуйста, введите натуральное число.")
        else: print(f"Последовательность чисел Фибоначчи до числа {n}:")
        for num in fibonacci_sequence(n): print(num, end='')
    except ValueError:
        (print("Пожалуйста, введите корректное число."))

main()
print('\n')

#Задача 2
def cyclic_sequence(n, sequence):
    while True:
        for num in sequence:
            if n <= 0:
                return
            yield num
            n -= 1

def cycle():
    try:
        n = int(input("Введите количество чисел для вывода в циклической последовательности: "))
        if n <= 0:
            print("Пожалуйста, введите положительное число.")
            return
        sequence = [1, 2, 3]
        cyclic_gen = cyclic_sequence(n, sequence)
        print("Циклическая последовательность:")
        for num in cyclic_gen:
            print(num, end=' ')
    except ValueError:
        print("Пожалуйста, введите корректное число.")
cycle()