
class Person:
    def __init__(self, _name ,_age):
        self.name =_name
        self.age =str(_age)

    def sayHi(self):
        print("Hello, my name is " +self.name +" and I am " +self.age + " years old!")

person1 = Person ('Bob', str(16)) 
person1.sayHi()

person2= Person ('James', str(22))
person2.sayHi()