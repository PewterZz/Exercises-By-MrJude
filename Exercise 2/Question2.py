# Question2
x = eval(input("Enter length of edge1: "))
y = eval(input("Enter length of edge2: "))
z = eval(input("Enter length of edge3: "))
if x+y > z and x+z > y and y+z > x:
    print(f"Perimeter is {x+y+z}")
else:
    print("Perimeter could not be calculated: The input is invalid")
