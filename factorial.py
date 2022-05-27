number =int(input("enter the number"))
factorial = 1
if number < 0:
     print("The factorial of negative numbers does NOT exist")
elif number== 0:
    print("factorial of 0=1")
else:
     for i in range(1,number+1):
         factorial=factorial*i
print ("The factorial of number is:",(factorial))