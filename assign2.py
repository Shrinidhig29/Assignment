""" Write a python program to accept the user's first and last name and then getting them printed in the reverse order
 with a space between first name and lst name.  """

first_name = input("First name: ")
last_name = input("Last name: ")
full_name = first_name + " " + last_name
print(full_name)

rev_name = full_name[::-1]
print(rev_name)
