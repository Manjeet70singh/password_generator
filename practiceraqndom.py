'''a,b=1,2
d=e=f=89
print(a)
print(b)
print(f)
print(e)

# += meaning is x=x+2

x=15
y=16
print(x==5)
print(x==15 and y==16)

s="helloplu"
print(s[0])
print(s[0:4])
print(s[0:-1])
print(s[0:-3])
print(s[::-1])  # for reverse the string

print(s.replace("l","o"))   # replace all l with o

'''

import random

passwordLength = int(input("Enter password length(Minimum 12):"))
digits = "0123456789"
specialCharacters = "!@#$%&*"
LowerCase = "qwertyuiopasdfghjklzxcvbnm"
UpperCase = "QWERTYUIOPASDFGHJKLZXCVBNM"
Concatenation = digits + specialCharacters + LowerCase + UpperCase

while passwordLength > 11:
    password = ""
    for i in range(passwordLength):
        password += random.choice(Concatenation)
    if ((char in specialCharacters for char in password) and
            (char in digits for char in password) and
            (char in LowerCase for char in password) and
            (char in UpperCase for char in password) and
            (len(password) >= 12)):
        print("Random Password: " ,password)
        break
else:
    print("INVALID")

