# Q6. leap year
# year = int(input("Enter your year here :"))
# if (year % 100 == 0 and year % 4 == 0) or year % 400 == 0:
#     print("Leap year")
# else:
#     print("not a leap year")

# type 2
# print("leap year") if (year % 100 == 0 and year % 4 == 0) or year % 400 == 0 else print("not a leap year")





# Q7. triangle  basic formula two sides of triangle must be greater than third side in all sides to check
 
# side_1 = float(input("Enter the length of side one :"))
# side_2 = float(input("Enter the length of side two :"))
# side_3 = float(input("Enter the length of side three :"))

# if (side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_3 + side_1 > side_2):
#     print("its a triangle")
# else:
#     print("not a triangle")


# type 2:
# print("Its a triangle") if (side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_3 + side_1 > side_2) else print("not a triangle")

# advanced method of input
# side1,side2,side3 = map(float,input("Enter sides of trainglr").split(","))






#Q8: vowel or consonant or neither

# letter = input("Enter the input : ").lower()
# if len(letter) > 1 or len(letter)< 1:
#     print("please give one character")
# elif letter in "aeiou":  --- you can write letter in ["a","i","e","o","s"]
#     print("its a vowel")
# else:
#     print("Its a consonant")


# if letter in ["a","e","i","o","s"]:
#     print("its a vowel")
# else:
#     print("its a consonant")


# advanced
# letter = input("Enter the input : ").lower()
# if len(letter) != 1:
#     print("please give one character")
# else:
#     if letter in "aeiou":
#         print("its a vowel")
#     elif letter.isalpha():
#         print("is consonant")
#     else:
#         print("its a special character")

