class Employee:
    def __init__ (employee ,_name, _salary,_id):
        employee.name= _name
        employee.salary = _salary
        employee.id= _id
    def emp(employee):
          print (f"Hi i am {employee.name} +ID no{employee.id} and I am paid KSH {employee.salary}")

employee1 = Employee (" Hamisa", str(3000))
employee1.emp()
              