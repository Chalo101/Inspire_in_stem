#geometric progression


a = (int(input("enter starting number:"))) 
r = (int(input("enter common ratio:")))
n = (int(input("enter n th term:"))) # N th term to be find

def printGP(a, r, n):
    for i in range(0, n):
        curr_term = a * pow(r, i)
        print(curr_term, end =" ")

printGP(a, r, n)