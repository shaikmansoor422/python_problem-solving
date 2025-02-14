

# num1 = int(input("enter the starting :"))
# num2 = int(input("enter the last :"))
# for p in range(num1,num2+1):
#     count =0
#     for i in range(1,p+1):
#         if p % i == 0:
#             count +=1
#     if count == 2:
#         print(p)
#     else:
#         pass


# lower order prime
# num = int(input("enter the prime numbr :"))
# if num >= 3:
#     while True:
#         count = 0
#         num -=1
#         for i in range(1,num+1):
#             if num % i == 0:
#                count +=1
#         if count == 2:
#             print(num)
#             break
    
# else:
#     print("give more than 3")



#both orders and nearest prime number



num = int(input("Enter the prime number"))
upp_num =0
low_num = 0
while True:
        count1 =0
        num +=1
        for i in range(1,num+1):
            if num % i ==0:
                count1 +=1
        if count1 == 2:
            upp_num = num
            break

while True:
    count2 =0
    if num > 3:
        num -=1
        for i in range (1,num+1):
            if num % i == 0:
                count2 +=1
        if count2 == 2:
             low_num = num
             break
upper = upp_num - num
lower = num - low_num

if low_num > upp_num:
    print("the nearest numbr is :",upp_num)
else:
     print("the nearest number is :", low_num)

            
                    
               