# lesson 7 on dictionaries
#!usr/bin/python

################################################################################
  #Dictionaries
  #Name :Charles Kagoko
  #Date :23/5/2022
#####################################################################


#Initializing Dictionaries

student= {"Name":"Charles","Age":19,"Gender":"Male"}

print(student['Name'])
print(student['Age'])
print(student['Gender'])

student["id_no"]="336687"
student["Hobby"]="Coding"
student["Club"]="Man u"
student["fav_colour"]="Blue"
print(student)
 
 # empty dictionary
#  use curly braces with empty
student= {}
student["fav_food"]='Chapati'
student['home_city']='Nairobi'
print(student)

 #modifying
student["Age"]=23
print(student)
del student['fav_food']
print(student)