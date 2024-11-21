#!/usr/bin/python3
a = 10
b = 9
if a > b:
    print("a is greater than b")
print("not sure if a is less than b")

c = 3
d = 3
if c < d:
    print("c is less than d")
elif c == d:
    print("c is equal to d")
else:
    print("c is greater than d")

e = 10
f = 10
if e == f:
    print("e is equal to f")
else:
    if e > f:
        print("e is greater than f")
    else:
        print('e is less than f')
