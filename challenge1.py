# write a prgram to check if a number is divicible by 5 or 7

number=int(input("Enter a number:"))
if (number %5 ==0):
   print(number, "is divisible by 5")

elif(number %7 ==0):
   print (number, "is divisible by 7")
 
elif (number %5 ==0) or (number%7 ==0):
   print (number,"is divisible by both 5 and 7")

else:
    print(f'{number} is not divisible by 5 or 7')



    


