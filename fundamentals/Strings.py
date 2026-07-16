# ---------- Strings ----------

# taking input
str1 = input("Enter first name: ")
print(len(str1))


# creation & type
str1 = "this is a string"
print(type(str1))


# concatenation
str2 = 'hello'
str3 = " 4"
print(str2 + str3)


# escape character (\n = new line)
print(str1 + "\n" + str3)


# length
print(len(str2))


# indexing
a = "Apna_College"
print(a[0])       # A  -> positive indexing starts from 0
print(a[4])       # _


# negative indexing
print(a[-1])      # e  -> last character (starts from -1)
print(a[-12])     # A  -> first character from the end


# slicing
print(a[0:4])      # Apna
print(a[0:])       # Apna_College
print(a[:9])       # Apna_Coll


# string methods
text = "i am studying python from apna college"

print(text.endswith("ap"))       # endswith() -> checks if string ends with given text (True/False)
print(text.capitalize())         # capitalize() -> makes first letter capital, rest lowercase
print(text.replace('a', 'G'))    # replace(old, new) -> replaces all occurrences of old with new
print(text.find("python"))       # find() -> returns index of first occurrence, -1 if not found
