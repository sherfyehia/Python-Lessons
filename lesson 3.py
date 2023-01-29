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


##############################Python While Loop ############################
print("##############################Python While Loop############################")

i = 1

while i <= 10:
    print(i)
    i = i + 1


print("the loop has ended")


# while True:
#     print(i)
#     i = i + 1

# print("infinite loop")

k = 1

while k <= 10:
    print(k)
    k = k + 1

else:
    print("k become more than 10 so the condition become false")

print("the loop has ended")

f = 1

while f <= 10:
    f = f + 1
    if f == 6:
        continue
    print(f)

print("we have skip number 6 using continue keyword")


b = 1

while b <= 10:
    b = b + 1
    if b == 6:
        break
    print(b)

print("we have break loop at number 6 using break keyword")


##############################Python For Loop ############################
print("##############################Python For Loop############################")

for letter in "sherifyehia":
    print(letter)


buddies = ['kira', 'light', 'misa', 'ryuk']

for char in buddies:
    print(char)


##############################print with len (number of variable) ############################
print("##############################print with len (number of variable)############################")

print(len(buddies))


for index in range(10):
    if index % 2 == 0:
        print(index, "is an even number")
    else:
        print(index, "is an odd number")


deathnote = ['kira', 'light', 'misa', 'ryuk']

for charaterics in range(len(deathnote)):
    if deathnote[charaterics] == 'ryuk':
        print(charaterics, 'is  ryuk')
    else:
        print(charaterics, 'in not ryuk')


##############################python power ############################
print("##############################python power############################")

print(2**3)


def power(base_num, pow_num):
    result = 1
    for index2 in range(pow_num):
        result = result * base_num
    return result


print(power(2, 3))
