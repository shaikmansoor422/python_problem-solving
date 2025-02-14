# functions

#questions 1: checking a number is prime or not
# def check_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True
# num = int(input("enter the number"))

# print("prime number")if check_prime(num) else print("not a prime")



# Question 2: checking a number is armstronwhere it is with in lower bound and upper bound
# mwthod 1:
# def arm_in_range(num):
#     last_num = 0
#     res = 0
#     temp = num
#     while temp > 0:
#         last_num = temp % 10
#         res += last_num ** len(str(num))
#         temp = temp // 10
#     return res == num

# ub = int(input("upper :"))
# lb = int(input("lower :"))

# for i in range(lb,ub+1):
#     if arm_in_range(i):
#         print(i)


# method 2
# def arm_num (lb,ub):
#     arm_numms = []
#     for num in range(lb,ub+1):
#         last_digit = 0
#         res = 0
#         temp = num
#         while temp > 0:
#             last_digit = temp % 10
#             res += last_digit ** len(str(num))
#             temp = temp // 10
#         if num == res :
#             arm_numms.append(num)
            
#     return arm_numms

# ub = int(input("upper :"))
# lb = int(input("lower :"))          
# result = arm_num(lb,ub )
# print(result)




