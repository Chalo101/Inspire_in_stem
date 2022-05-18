# Methods
from concurrent.futures.process import _chain_from_iterable_of_lists


name = "Mathenge Mugo"
name = "Ada Loveace"

user_name = "Lovelace "
age =15
person ="I am " +str(name)+ " and my age is "+ str(age)
# print (person)
# format metod
# print("My name is {} and I am {} years old " .format(name , age))
#new line and tab \t
#print (f"my \t name is {name} \n and I am {age} years old")
print(user_name.rstrip())
msg = ''' QRST126XDG MPESA CONFIRMED
          you have received ksh 2300
          from James Muoki
          18th May 2022
          Safaricom transport for you
           '''
print (msg)
txt = '''My name is Charles Kagoko'''
print (txt)

#slice
city = "Nairobi"
print(city[:5])

f_name = "charles kagoko" #small letters
print(f_name.upper())

# .lower() convert to lower case
s_name = "CHARLES KAGOKO"
print(s_name.lower())

#concatination  converting from one data type to another
# int -> float   float(x)
#float -> int   int(x)
#int -> string  str(x)
number =6

print(str(number))

x = 4# x is an intager
print(float(x))

y = 3.24
print(int(x))
f_name = "Charles"

s_name = "Kagoko"

full_name =f_name + s_name

print(full_name)

#replace
name= "Charles"
print (name.replace('C', 'g'))

msg = "hello from Charles Kagoko how are you"
print(msg.split()) 

print(len(msg))