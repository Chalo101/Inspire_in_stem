# first n terms of an AP
# a =first_number
# d=(common_difference)
# use loops

#Arithmetic progression 

a=int(input("Enter the first number"))
d=int(input("Enter the common difference"))
n=int(input("Enter the number"))
for i in range(1,n+1):
    n_term= a+(i-1)*d
    print(n_term)
sum_n=(n_term/2)*(2*a+(n-1)*d)
print("The sum of numbers is :",(sum_n))