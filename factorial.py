# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)


# # num = int(input("Enter a number: "))
# # print("Factorial of", num, "is:", factorial(num))
# print(factorial(5))

x = int(input("enter anumber:"))

fact = 1
if  x>0:
    for i in range(x,1 ,-1):
        fact = fact*i
print(fact)
