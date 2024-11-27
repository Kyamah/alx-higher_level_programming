#!/usr/bin/python3

#modulo operator are used to check multiples of numbers

print(4 % 3)

#list numbers for range

print(list(range(1, 21)))

#add numbers for multiples of 3

total = 0
for y in range(1, 21):
    if y % 3 == 0:
        total += y
print(total)

#add numbers for multiples of 3 and 5

total1 = 0
for z in range(1, 100):
    if z % 3 == 0 or z % 5 == 0:
        total1 += z
print(total1)
