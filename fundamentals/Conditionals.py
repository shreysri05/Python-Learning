# ---------- Conditionals ----------

# if / elif / else -> checking eligibility based on age
age = int(input("Enter age: "))

if age > 21:
    print("eligible to vote and license")        # age > 21
elif 18 <= age < 21:
    print("eligible to vote not license")        # 18 <= age < 21
else:
    print("You are not eligible for both")        # age < 18


# if / elif / else -> grading system based on marks
marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")                # 90 and above
elif marks >= 80:
    print("B")                # 80 - 89
elif marks >= 70:
    print("C")                # 70 - 79
elif marks >= 60:
    print("D")                # 60 - 69
elif marks >= 50:
    print("E")                # 50 - 59
else:
    print("F")                 # below 50


# Q1: check whether number entered by user is odd or even
num = int(input("Enter number: "))

if num % 2 == 0:
    print(num, "is even")     # remainder 0 -> even
else:
    print(num, "is odd")      # remainder 1 -> odd


# Q2: find the greatest of three numbers using nested if-else
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a > b:
    if a > c:
        print(a, "is greatest")   # a > b and a > c
    else:
        print(c, "is greatest")   # a > b but c >= a
else:
    if b > c:
        print(b, "is greatest")   # b >= a and b > c
    else:
        print(c, "is greatest")   # b >= a but c >= b

# built-in shortcut (no need for nested if-else):
# print(max(a, b, c), "is greatest")


# Q3: check whether a number is a multiple of 7
a = int(input("Enter number: "))

if a % 7 == 0:
    print(a, "is a multiple of 7")       # remainder 0
else:
    print(a, "is not a multiple of 7")   # remainder != 0

# built-in alternative: divmod(a, 7) returns (quotient, remainder) in one go
# quotient, remainder = divmod(a, 7)
# if remainder == 0: ...
