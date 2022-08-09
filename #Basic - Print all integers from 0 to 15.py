#Basic - Print all integers from 0 to 150.
#=========================================
# for index in range (101):
#     if index <= 100:
#         print(index)

# =========================================
# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
# ========================================
# for index in range(1000):
#     if index % 5 == 0:
#         print(index)

# =========================================
# Counting, the Dojo Way - Print integers 1 to 100.
# If divisible by 5, print "Coding" instead. If divisible 
# by 10, print "Coding Dojo".
# =========================================

# def divid_by5_10():
# for index in range (1, 101):
#     if index + 1 > 0: 
#         print(index)
#     if index % 5 == 0:
#             print("Coding")
#     else index % 10 == 0:
#         print ("Coding Dojo")

# =========================================
# Whoa. That Sucker's Huge - Add odd integers from
#  0 to 500,000, and print the final sum.
# =========================================

# def odd():
# for index in range (0, 500000, ):
#     if index  % 2 == 0:
#         print(index)

# =========================================
# Countdown by fours  - Print positive numbers starting 
# at 2018, counting down by fours.
# =========================================

# def countdown():
# for index in range(2018, 0, -4):
#     print(index)

# =========================================
# Flexible Counter - Set three variables: lowNum, highNum, 
# mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the 
# loop should print 3, 6, 9 (on successive lines)
# =========================================

def flex_count(low = 3, high = 9, mult = 3):
    for index in range (low, high):
        if index % mult == 0:
            print(index)