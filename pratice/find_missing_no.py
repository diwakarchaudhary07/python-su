numbers = [1, 2, 3, 5]

n = len(numbers) + 1

for i in range(1, n + 1):
    if i not in numbers:
        print(i)
        break