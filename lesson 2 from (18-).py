##############################Escape series(18)############################
from math import *
print(
    "##############################Escape series############################")
print('learn \npython')
print('\N{copyright sign}SherifElyehia')
print('\N{registered sign}SherifElyehia')
print('\N{up down arrow}SherifElyehia')
print('\N{left right arrow}SherifElyehia')
print('\'sherifyehia\'')
print("sherif\a")
#################################input (19)###############################
print('############################ input (19)###############################')
'''
basic code for input:-
var=input()
'''
#name = input("Enter your name :")
#age = input("Enter your age :")
#print("welcome :" + name + "your age :" + age)
#################################String to Integer , Integer to String (20)###############################
print('###########################change String to Integer , Integer to String (20)###############################')
#age2 = input("enter your age: ")
# print(type(age2))
#age3 = int(input("enter your age: "))
# print(type(age3))
#################################convert string varible into integer###############################
print('##################################convert string varible into integer###############################')
# num1 = int(input('Frist number:'))
# num2 = int(input('second number:'))
# print(num1+num2)
#################################if conditions###############################
print('############################################if conditions###########################################')
"""
if condition
elif condition
else
"""
# x = 30
# y = 30
# if x > y:
#     print('yes it is x is bigger ')
# elif x < y:
#     print('yes that is true y is bigger')
# elif x == y:
#     print('x is equal to y')
# else:
#     print('try again')

# a = 10
# b = 5
# if a == 10 and b == 20:
#     print('yes it true')
# else:
#     print('that is wrong')

# if a == 10 or b == 20:
#     print('yes it true')
# else:
#     print('that is wrong')
###################################example if condition############
print("####################################example using if condition#############")
# speed = int(input('how much speed of your car?'))
# traffic = input('do you break the red light?')
# if speed > 100:
#     print('you will go to jail to incresing in speed')
# elif traffic == 'yes':
#     print('you will go to jail for break red light')
# else:
#     print('thanks for respect')
###################################using /n /t /a############
print("####################################using /n /t /a#############")
print('sherif \nyehia \tmostafa \arezq')
##################################colors###############################
print('##################################colors###############################')
print('\033[1;30;40mSheirf Yehia')
print('\033[1;31;40mSheirf Yehia')
print('\033[1;32;40mSheirf Yehia')
print('\033[1;33;40mSheirf Yehia')
print('\033[1;34;40mSheirf Yehia')
print('\033[1;35;40mSheirf Yehia')
print('\033[1;34;40mSheirf Yehia')
##################################range###############################
print('##################################range###############################')
print(range(10))
print(range(5, 10))
print(list(range(1, 100)))
##################################characters###############################
print('##################################characters###############################')
for i in range(ord('a'), ord('z')):
    print(chr(i))
################################strings lower/upper case###########################
print('################################strings lower/upper case###########################')
text = ("Abcde is english letter")
print(text.lower())
print(text[3])
print(text.replace("english", "arabic"))
my_num = -5
print(str(my_num) + " is my favourite number")
print(abs(my_num))
print(str(pow(2, 3)) + "power")
print(str(max(10, 5)) + "max")
print((str(min(10, 8))) + "min")
print((str(round(3.7))) + "round")
print((str(round(3.4))) + "round")
print((str(floor(3.7))) + "floor")
print((str(ceil(3.2))) + "ceil")
################################varible list###########################
print('################################varible list###########################')
friends = [1, 'sherif', 'amr', True, False]
print(friends[2])
############################# add value to variable list#######################
print('############################# add value to variable list #######################')
add_value_to_variable = ['sherif', 'yehia', 'mostafa', 'khtab', 'khtab']
add_value_to_variable.append('Rezq')
print(add_value_to_variable)
add_value_to_variable.insert(1, "sheko")
print(add_value_to_variable)
add_value_to_variable.remove('sherif')
print(add_value_to_variable)
add_value_to_variable.pop()
print(add_value_to_variable)
print(add_value_to_variable.index('yehia'))
print(add_value_to_variable.count('khtab'))
add_value_to_variable.clear()
print(add_value_to_variable)
############################# copy value of varible#######################
print('############################# copy value of varible#######################')
all_name = ['sherif', 'yehia', 'mostafa']
copy_of_all_name = all_name.copy()
print(copy_of_all_name)
