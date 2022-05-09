"""Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 ,
between 2000 and 32000(both include). The numbers obtained should be printed in a comma separated sequences on a
single line"""

var_num = int(input("Choose numbers: "))

if 1999 < var_num < 3201:
    # print(f'var_num:', var_num)
    if (var_num % 7==0) and (var_num % 5!=0):
        # print(f'var_num:', var_num)
        
        lst_numbers = []

        for i in range(0, var_num):
            num = int(input())
            lst_numbers.append(num)
        print(lst_numbers)

    else:
        print("fail")
else:
    print("You have choose a wrong number")
