n = int(input('Введите число '))
counter = 0
while n != 1:
    if n % 2 == 0:
        n = n / 2
        counter += 1
        print(n)
    elif n % 2 != 0:
        n = 3 * n + 1
        counter += 1
        print(n)
print(f'Количество действий: {counter}')
