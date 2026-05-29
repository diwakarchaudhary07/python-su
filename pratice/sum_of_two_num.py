def cal ():
    x = int(input("Enter your number1: "))
    y = int(input("Enter your number2: "))
    
    print("1 .addition:")
    print("2 .substraction:")
    print("3 .multiplication:")
    print("4 .division:")
    
    
    def calculator():
        user = int(input("Enter your choice :" ))
        if user == 1 :
            print(x+y)
             
        elif user == 2 :
              print(x-y)
        elif user == 3 :
             print(x*y)
                
        elif user == 4 :
             print(x/y)
        else:
            print("invalid choice:")
        
    print(calculator())
                   
print(cal())
user2 = input("if you want again perform calculation ! n/y :") 
if user2 == "y":
     print(cal())
else:
     print("Thank you !")
