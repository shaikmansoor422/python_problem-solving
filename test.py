#  question 1 :# A wizard gives you a magic number and asks you to guess if 
# it’s divisible by 3 and 5. If it is, print "FizzBuzz". 
# If it’s only divisible by 3, print "Fizz". If it’s only 
# # divisible by 5, print "Buzz". Otherwise, print the number itself


# num = int(input("Enter the number :"))
# if num <= 0 :
#     print("please entre a positive number")
# else:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FIZZBUZZ")
#     elif num % 3 == 0 :
#         print("FIZZ")
#     elif num % 5 == 0:
#         print("BUZZ")
#     else:
#         print("not a FIZZ, not a BUZZ and not a FIZZBUZZ")




# question 2
# Battle of the Warriors
# Two warriors are fighting in a game. Each has health and attack power. The warrior with the higher attack power wins unless both have the same attack power, in which case the one with higher health wins. If both health and attack power are the same, print "Draw".

# war1_health= int(input("First warrior health : "))
# war1_power = int(input("First warrior power : "))
# war2_health = int(input("Second warrior health :"))
# war2_power = int(input("Second warrior power : "))
# if war1_health <= 0 or war1_power <= 0 or war2_health <= 0 or war2_power <= 0:
#     print("Please enter the positive health and power")
# else: 
#     if war1_health > war2_health and war1_power == war2_power :
#        print("Warrior one won")
#     elif war2_health > war1_health and war1_power == war2_power :
#        print("Warrior two won")
#     elif war1_health == war2_health and war1_power > war2_power :
#        print("Warrior one won")
#     elif war1_health == war2_health and war1_power < war2_power :
#        print("Warrior two won")
#     elif war1_health == war2_health and war1_power == war2_power :
#        print("DRAW")




# question 3:
# balance = int(input("Enter your balance :"))
# amount = int(input("Please enter the amount (must be multiple of hundred) : "))
# if amount > 0:
#    if amount % 100 == 0:
#       if amount <= balance :
#          print("your transaction is succeful")
#       else:
#          print("Sorry, your balance is low")
#    else:
#       print("Please enter amount in multiples of hundred")
# else:
#    print("please enter positive amount")  


#  4 question for  password creating?
# # pswd = input("Enter your password")
# # if (pswd > 8) and (pswd in "!@#$%^&*()_+{}[]~`;:'""<>,.?/") and (pswd.isalpha) and (pswd.isnumeric()) and (pswd.upper()) and (pswd.lower()):
# #     print("strong password")
# # else:
# #     print("week passwrod")


# Question 5: 
# The Triangle Validator ▲
# You are given three sides of a triangle. First, check if they form a valid triangle (sum of any two sides > third side).
# • If valid, classify it as:
# • Equilateral (all sides equal)
# • Isosceles (two sides equal)
# Scalene (all sides different)
# If not valid, print "Not a Triangle".
# js
# // Sample Input: 3, 4, 8
# // Sample Output: "Not a Triangle"
# Copy
# Edit


tri1  = int(input("Enter triangle side1 :"))
tri2  = int(input("Enter triangle side2 :"))
tri3  = int(input("Enter triangle side3 :"))


if ( tri2 + tri3 > tri1 ) and (tri3 + tri1 > tri2  ) and (tri2+tri1 > tri3):
   if (tri1 == tri2 == tri3):
      print("Equivaletaral triangle")
   elif tri1 == tri2 or tri2 == tri3 or tri3 == tri1:
      print("Isosceles trianlge")
   else:
      print("scalene")
else:
   print("Its not a triangle please give valid inputs")