"""Write a python program to find the volume of a sphere with diameter 12cm
V = 4/3*pi*r^2"""

dia_sphere = input("Diameter: ")
# rad_sphere = input("radius of sphere: ")
rad_sphere = int(dia_sphere)//2
"""def cube(x):
    return x*x*x
n = int(input("enter the number: "))"""
# pi = int(input("write a value for pi: "))
volume_sphere = 4/3*3.1415*rad_sphere*rad_sphere*rad_sphere
# volume_sphere = 4/3*3.1415*cube(n)
print(volume_sphere)
