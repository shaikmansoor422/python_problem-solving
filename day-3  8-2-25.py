# # loops

# # . Loops:
# a. Easy Questions:
# i.    Print all numbers from 1 to 100 using a for loop.
# ii.    Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
# iii.    Print all even numbers between 1 and 50 using a while loop.
# iv.    Write a program to display the multiplication table of a given number. First 20
# v.    Reverse a number using a while loop.
# 1. Also can we get the sum of all the digits.
# vi.    Write a program to count the number of digits in a given number using a while loop.
# vii.    Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.
# b. Medium Questions: 
# i.    Print the first 10 terms of the Fibonacci series using a for loop.
# ii.    Check if a given number is a prime number using a for loop.
# iii.    Write a program to calculate the factorial of a number using a while loop.
# iv.    Print all numbers from 1 to 100 that are divisible by 3 and 5 using a for loop.
# v.    Implement a menu-driven program where the user can choose to:
# 1. Find the square of a number.
# 2. Find the cube of a number.
# 3. Exit.
# vi.    Implement a basic login system where the user has three attempts to enter the correct password using a loop.




# i.    Print all numbers from 1 to 100 using a for loop.\

# for i in range(1,101):
#     print(i)


# i= 1
# while i <= 100:
#     print(i)
#     i+=1


# printing even and oddds 

# for i in range(0,101,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)



# question 2 : # ii.    Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)


# num = int(input("Enter number :"))
# sum = 0
# for i in range(0,num+1):
#     sum= sum+i
# print(sum)


# num = int(input("Enter number :"))
# sum = (num*(num+1))/2
# print(int(sum))


#Question  iii.    Print all even numbers between 1 and 50 using a while loop.

# i = 0
# while i<=50:
#     print(i)
#     i+=2

# i = 0
# while i <=50:
#     if i % 2 ==0:
#         print(i)
#     i +=1

#  QUeston4 iv.    Write a program to display the multiplication table of a given number. First 20

# i = 3
# for j in range(0,21):
#     print(i,"X",j,"=",i*j)

# i = int(input("enter the table you want :"))
# for j in range(0,21):
#     print(i,"X",j,"=",i*j)


# question 5.    Reverse a number using a while loop.

# metod :1
# number = 123456
# str_num = str(number)
# rev_num = ""
# for i in range(len(str_num)-1,-1,-1):
#     rev_num += str_num[i]
# print(rev_num)


# method : 2
# num = 12345678
# rev_num = 0
# while num > 0:
#     last_num = num % 10
#     rev_num  = rev_num * 10 + last_num
#     num = num // 10
# print(rev_num)


# checking a number is palindrome or not
# num = int(input("enter the number"))
# rev_num = 0
# temp = num
# while num > 0:
#     last_no = num % 10
#     rev_num = rev_num * 10 + last_no
#     num = num // 10
# if temp == rev_num :
#     print("palendrome")
# else:
#     print("not a palindrome")


# checking the sum and number of digits


# num = int(input("enter the number"))
# rev_num = 0
# count = 0
# sum = 0
# temp = num
# while num > 0:
#     last_no = num % 10
#     sum += last_no
#     count +=1
#     rev_num = rev_num * 10 + last_no
#     num = num // 10
# print(count)
# print(sum)
# if temp == rev_num :
#     print("palendrome")
# else:
#     print("not a palindrome")




#giving 3 chances to user for password entering
# user_name = "Mansoor"
# psswd = 11111

# attempts = 3
# while attempts > 0:
#     print("Enter username and pasword---")
#     print("but the attempts you have are :", attempts)

#     name_input = input("Enter the name :")
#     pswd_input = int(input("Enter the password :"))

#     if user_name == name_input and int(pswd_input) == psswd :
#         print("Login Succesful")
#         break
#     else:
#         print("Wrong credential")
#         attempts -=1


#  IMplement a menu -driven program where the user can choose to :
# 1 find the square of a number
# 2find the cube of a number
# and 3 exit

# while True:
#     print("Choose the options : '1' for square value and '2' for cube value or enter 'exit' to get exit")
#     opt = input("Enter the value('1','2','exit') :").lower()
#     if opt == "1":
#         res = 0
#         num = int(input("Enter the number :"))
#         res = num ** 2
#         print("the result",res)
#     elif opt == "2":
#         res = 0
#         num = int(input("Enter the number :"))
#         res = num ** 3
#         print("the result",res)
#     elif opt == "exit":
#         print("the game is over")
#         break
#     else:
#         print("Invalid choice! Please enter '1', '2', or 'exit'.")



# ii.    Check if a given number is a prime number using a for loop.

# while True:
#     num = int(input("Enter the numbr :"))
#     couhnt = 0
#     for i in range(1,num+1):
#         if num % i == 0:
#             couhnt += 1
#     if couhnt == 2:
#          print("its a prime")
#     else:
#           print("not a prime")

