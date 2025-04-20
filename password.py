import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers= "0123456789"
symbols= "!@#$%^&*()_+=?><[]"

all_charts=lower+upper+numbers+symbols
length=int(input("enter a length: "))

password= ''.join(random.sample(all_charts, length))
print("Generated password:", password)