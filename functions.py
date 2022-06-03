#function parameters
# x=4
# y=5
# def add_numbers (x,y):
#     add_numbers = x+y
# print("The sum of numbers",add_numbers)
# add_numbers (20,40)
# add_numbers (70,50)
# add_numbers (1,4)

# def products_numbers(x,y):
#     products_numbers =x*y
#     print("the product of numbers: ",products_numbers)
# products_numbers(2,5)
# products_numbers(3,6)
# products_numbers(78,14)
# products_numbers(45,1)
# products_numbers(36,4)

#  Ussing default parameters
def print_name (name ="Charles Kagoko"):
    print(name)

print_name("Joseph")

# return from a function

def get_sum (num1,num2):
    sum_nums=num1+num2
    return sum_nums
print (get_sum(7,12))


# Write a functin to get the powers of numbers
def get_powers(number,power):
    power_num =(number**power)
    return power_num
print (get_powers(6,4))


def get_full_name(f_name,s_name):
    full_name =(f_name+" " +s_name)
    return full_name.title()
print (get_full_name("Charles", "Kagoko"))


# Retufning a dictionary from a function

def create_full_name(f_name,s_name):
    person={'first':f_name,'second':s_name}
    return person

student = create_full_name('Chalo','Kagoko')
print(student)