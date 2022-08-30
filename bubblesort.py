array = [4, 10, 5, 8, 1, 2, 3, 9, 6, 7]

for i in range(len(array) - 1):
    for j in range(len(array) - 1):
        num1 = array[j]
        num2 = array[j + 1]
        if num1 < num2:
            continue
        else:
            array[j] = num2
            array[j + 1] = num1

print(array)
