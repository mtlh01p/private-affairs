import math
radiusString = input("Enter the radius of your circle: ")
radiusFloat = float (radiusString)
circumference = 2 * math.pi * radiusFloat
area = math.pi * radiusFloat * radiusFloat

print()
print("The circumference of your circle is: ", circumference, \
      ", and the area is: ", area)
