##############################if condition############################
print("##############################if condition############################")

# = used to defined the variable with value
# == worked as a equal statment

are_you_hungry = True
are_you_not_hungry = False

if are_you_hungry == True and are_you_not_hungry == False:
    print('go eat')
elif are_you_hungry == False and are_you_not_hungry == True:
    print('iam not hungry')
elif not are_you_hungry == True and are_you_not_hungry == False:
    print('iam not hungry')
else:
    print('iam hungry and iam not hungry')


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(50, 5, 10))


def match_string(str1, str2):
    if str1 == str2:
        print('the string  do match')
    else:
        print('the string dont match')


match_string('sherif', 'yehia')


def match_string2(str3, str4):
    if str3 != str4:
        print('the string  do match')
    else:
        print('the string dont match')


match_string2('sherif', 'yehia')


##############################calculator project ############################
print("##############################calculator project############################")

# number1 = float(input('please enter the frist number :'))
# operator = input('please enter the operator: ')
# number2 = float(input('please enter the second number: '))

# if operator == '+':
#     print(number1 + number2)
# elif operator == '-':
#     print(number1 - number2)
# elif operator == '/':
#     print(number1/number2)
# elif operator == '*':
#     print(number1 * number2)
# else:
#     print('wrong operator')

##############################Python Dictionaries ############################
print("##############################Python Dictionaries############################")
convert_month = {
    "jan": "january",
    "feb": "febraury",
    "mar": "march"
}

print(convert_month["mar"])
print(convert_month.get("feb"))
print(convert_month.get("apr", "there is not value here"))
