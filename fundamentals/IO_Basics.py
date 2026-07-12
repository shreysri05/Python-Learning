 # ---------- INPUT / OUTPUT BASICS ----------

# 1. Basic Output
print("Hello, World!")
print("Multiple", "values", "print")

# 2. Basic Input
name = input("Enter your name: ")
print("Hello,", name)

# 3. Input with type conversion
age = int(input("Enter your age: "))
print("You will be", age + 1, "next year")

# 4. Multiple inputs in one line
a, b = input("Enter two numbers separated by space: ").split()
print("First:", a, "Second:", b)

# 5. f-strings (formatted output)
city = input("Enter your city: ")
print(f"{name} is {age} years old and lives in {city}")

# 6. print() with sep and end parameters
print("Python", "is", "fun", sep="-")
print("Hello", end=" ")
print("World")

# 7. Taking float input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters")

# 8. Simple calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

# 9. Decimal places control (f-string)
price = 99.98765
print(f"Price: {price:.2f}")

# 10. Old-style formatting (just to know, not preferred)
print("My name is %s" % name)
