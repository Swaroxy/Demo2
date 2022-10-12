#Str Class
str1 = "PCPS College"
print(str1)
print(type(str1))
print(id(str1))
print(len(str1))
print(min(str1))
print(max(str1))

#indexing
str1 = "PCPS College" #Extract
print(str1[0])
print(str1[-3])


#slicing
str1 = 'object does not support item assignment'
str2 = str1[::-1]
print(str2)
print(id(str1))
print(id(str2))

#Explore Str class
str1 = 'object does not support item assignment'
print(help(str1))

#Capitalize
str1 = 'object does not support item assignment'
str2 = str1.capitalize()
print(id(str2))
print(id(str1))
print(str2)

#Upper
str1 = 'object does not support item assignment'
str2 = str1.upper()
print(str1)
print(str2)

#Lower
str1 = 'object does not support item assignment'
str2 = str1.lower()
print(str1)
print(str2)

#Casefold
str1 = "Admin"
str2 = "ADMIN"
if(str1 == str2):
    print("True")
else:
    print("False")
str1 = str1.casefold()
str2 = str2.casefold()
print(str1, str2)
if str1 == str2:
    print("True")
else:
    print("False")

#Center
str1 = "123456"
str2 = str1.center(20, '*')
print(str2)

