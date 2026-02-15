print("Hello, World!")
print(3)

a = 5
print(a)

b = "Michael"
print(b)

print(a,b)

print(type(a))
print(type(b))
print(type(9.0))
print(type(True))# :)

#Hello, World!

print(5 + 5)
print(5 - 5)
print(a - 5)

c = 3
d = 4
e = 5
f = 6

g = c + d ** e / f % e

h = c - d // e ** (f + d) * c

#0. Parentheses: ()
#1. Powers/Exponents: **
#2. Products: */ // %
#3. Addition: + -

print(h)

# Lists
l = [1, 2, 3,5]
print(l[3])

m = [1, 2, 3, "five", 6.0]
print(m)

# String formating
age = 5
print("My age is:",age)
# "I am 5 years old"
# "I am not 5 years old"
st = "I am"
st1 = "not"
st2 = "years old"
print(st, age, st2)
print(st, st1, age, st2)

print()

st_f = "I am {} years old"
#st_f1 = "I am not {} years old"
st_not_f = "not"
print(st_f.format(age, ""))
#print(st_f1.format(age))
print(st_f.format(st_not_f, age))

# User Input
age1 = input("Please enter your age: ")
age1 = int(age1)
print(age1)
print(type(age1))

print("In 1 year, you will be {} years old".format(age1 + 1))