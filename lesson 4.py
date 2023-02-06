##############################Python 2D Lists & Nested Loops ############################
print("##############################Python 2D Lists & Nested Loops############################")
no_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(no_list[2])
print(no_list[2][1])  # print row number 2 and colum number 1

for row in no_list:
    print(row)

for row in no_list:
    for column in row:
        print(column)
############################## comments ############################
print("############################## comments ############################")
# comments

'''
the
is
comments
'''
############################## Python Errors (try)(except) ############################
print("############################## Python Errors (try)(except) ############################")
# try:
#     value = int(input("Enter a number:"))
#     print(value)
# except:
#     print('invalid input')  # if you enter a string

############################## Python Errors (try)(except) ############################
print("############################## Python Errors (try)(except) ############################")

# try:
#     value2 = int(input("Enter a number:"))
#     print(value2)
#     result = 10/0
# except ZeroDivisionError:  # using to handle spacify error
#     print('you cannot divide by zero')
# except ValueError:  # using to handle spacify error
#     print('invalid input')

############################## Python Errors (try)(except with as) ############################
print("############################## Python Errors (try)(except with as) ############################")

# try:
#     value2 = int(input("Enter a number:"))
#     print(value2)
#     result = 10/0
# except ZeroDivisionError as err:  # using to handle spacify error
#     print(err)
# except ValueError as err2:  # using to handle spacify error
#     print(err2)

############################## Python Reading Files ############################
print("############################## Python Reading Files ############################")
workers_file = open("worker.txt", "r")
print(workers_file.readable())
workers_file.close()

workers_file2 = open("worker.txt", "r")
print(workers_file2.read())
workers_file2.close()


workers_file3 = open("worker.txt", "r")
print(workers_file3.readline())
print(workers_file3.readline())
workers_file3.close()

workers_file4 = open("worker.txt", "r")
print(workers_file4.readlines())
workers_file4.close()


workers_file5 = open("worker.txt", "r")
for worker in workers_file5.readlines():
    print(worker)
workers_file5.close()


############################## Python Writing Files ############################
print("############################## Python Writing Files ############################")
