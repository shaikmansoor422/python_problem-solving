# 1. code to find min value, max value and sum of elements in from a list
# 2. take 2 numbers , add, multiply,divivde and exponent them and floor division without function and with function
# 3. take two ages of persons as input and print whos age is older

#1
#code to find min value, max value and sum of elements in from a list
# list = [1,4,7,-35,25,4,6]
# max_value = list[0]
# min_value = list[0]
# sum = 0
# for i in range(0, len(list)):
#     if list[i]>max_value:
#         max_value = list[i]
#     if  list[i] < min_value:
#         max_value = list[i]
#     sum += list[i]

# print(max_value)
# print(min_value)
# print(sum)


#2
#take 2 numbers , add, multiply,divivde and exponent them and floor division without function and with function
# a = 10
# b = 20
# print(a+b)
# print(a-b)
# print(a*b)
# print(a%b)
# print(a/b)
# print(a//b)
# print(a**b)

# def evalutate(a,b):
#     # print(a+b) 
#     # print(a-b)
#     # print(a*b)
#     # print(a%b)
#     # print(a//b)
#     # print(a/b)
#     # print(a**b)
#     add = a+b
#     sub = a-b
#     divi = a/b
#     mul = a*b
#     modul = a%b
#     return add,sub,divi,mul,modul
# print(evalutate( 10, 20))




# 3. take two ages of persons as input and print whos age is older

# ramesh = int(input("Enter the age of ramesh : "))
# suresh = int(input("Enter the age of suresh : "))
# if ramesh > suresh:
#     print("ramesh is elder")
# elif ramesh == suresh :
#     print("ramesh and suresh age is same")
# else:
#     print("suresh is elder")

#answer 2:
#print("ramesh is elder ") if ramesh > suresh else print("suresh is elder")
#answer 3:
#res = "ramesh is elder " if ramesh > suresh else "suresh is elder"




# 4 . same queston for e persons

#answer 1:
# ramesh = int(input("Enter the age of ramesh : "))
# suresh = int(input("Enter the age of suresh : "))
# ganesh = int(input("Enter the age of ganesh : "))

# if ramesh > suresh and ramesh > ganesh:
#     print("ramesh is elder than ganesh and suresh")
# elif suresh > ramesh and suresh > ganesh:
#     print("suresh is elder than ganesh and ramesh")
# elif ganesh > suresh and ganesh > ramesh :
#     print('ganesh is elder than both')
# elif ramesh == ganesh and ramesh != suresh:
#     print("ramesh is age is equal to ganesh")
# elif ramesh == suresh and ramesh != ganesh:
#     print("ramesh is age is equal to suresh")
# elif suresh == ganesh and suresh !=ramesh:
#     print("suresh is age is equal to ganesh")
# else:
#     print("suresh , ganesh and ramesh ages are same")



# 5 . simple calculater:with 3 inputs

# operation = input("Enter the operation you want to do (add, mul, div, sub, modul) : ")
# value_1 = float(input("Enter the first value : "))
# value_2 = float(input("Enter the second value : "))

# opr = operation.lower()
# if opr == 'add' :
#     print(value_1+value_2)
# elif opr == 'mul':
#     print(value_1*value_2)
# elif opr == 'modul':
#     print(value_1%value_2)
# elif opr == 'sub':
#     print(value_1*value_2)
# else:
#     print(value_1*value_2) if value_2 > 0 else print("please give valid inputs")


# Q7. week display by number

# days ={
#     1:"monday",
#     2:"tuesday",
#     3:"wednesday",
#     4:"thursdday",
#     5:"friday",
#     6:"saturday",
#     7:"sunday"

# }

# num = int(input("enter a number from (1-7) : "))
# if num >=1 and num <=7:
#     print("the day is :",days[num])
# else:
#     print("invalid input")


# Q8. same for months also




