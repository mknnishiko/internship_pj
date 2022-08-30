array = [4, 10, 5, 8, 1, 2, 3, 9, 6, 7]

for i in range(len(array) - 1):
    for i in range(len(array) - 1):
        num1 = array[i]
        num2 = array[i + 1]
        if num1 < num2:
            continue
        else:
            array[i] = num2
            array[i + 1] = num1

print(array)
