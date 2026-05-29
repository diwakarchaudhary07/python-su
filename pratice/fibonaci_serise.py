n = int(input("Enter number of terms: "))

x = 0
y = 1

print("Fibonacci Series:")

for i in range(n):
    print(x, end=" ")
    
    z = x + y
    x = y
    y = z