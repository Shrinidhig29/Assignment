"""Create the below pattern using nested for loop in python
*
**
***
****
*****
****
***
**
*
# """
n = int(input("Enter the number of stars you want to draw: "))

for i in range(0, n, 1):
    print(i * '* ')
for j in range(n, 0, -1):
    print(j * '* ')

# ==========================================================================

# n = int(input("Enter the number to draw stars: "))
#
# for i in range(n):
#     for j in range(i):
#         print('*', end=' ')
#     print(' ')
#
# for i in range(n, 0, -1):
#     for j in range(i):
#         print('* ', end=' ')
#     print(' ')

