#!usr/bin/python
vehicles = ["bmw" ,"audi" ,"toyota", "mercedes", "jeep"]

# using a for loop to print all vehicles

for vehicle in vehicles:
    if (vehicle== "jeep"):
     print (vehicle.upper())

colours = ("blue","green","orange","purple","violet","yellow")
i=0
while i < len(colours):
    if colours[0] == "blue":
     print(colours[0].upper())
     i += 1


i=1
while i< len(colours):
    if colours[1]=="green":
        print(colours[1].upper())
        i += 1


i=2
while i < len(colours):
    if colours[2]== "orange":
        print(colours[2].upper())
        i += 1        


i=3
while i< len(colours):
    if colours[3]=="purple":
        print(colours[3].upper())
        i += 1        


i=4
while i < len(colours):
    if colours[4]=="violet":
        print(colours[4].upper())
        i += 1


i=5
while i < len(colours):
    if (colours[5]=="yellow"):
        print(colours[5].upper())
        i += 1         