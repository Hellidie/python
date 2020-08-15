N = int(input('Введите количество элементов массива: '))
arr = []

if 1 <= N <= 100:
    while len(arr) < N:
        arr.append(int(input('Введите элемент массива:')))
    for i in arr:
        if 1 <= int(i) <= 1000:
            continue
        else:
            print('Элементы не должны быть меньше 1 или больше 1000')
            quit()
    print(arr)
else:
    quit()

print('Максимальный элемент массива: ', max(arr))

arr.remove(min(arr))

print('Предпоследний по величине элемент массива: ', min(arr))
