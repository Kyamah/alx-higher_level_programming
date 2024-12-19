#!/usr/bin/python3

#adding a set of speficic numbers in a set. 
#adding a set of negative numbers.
 
given_list = [9, 7, 6, 4, 2, -3, -6, -8, -9]

total = 0
l = len(given_list) - 1
while given_list[l] < 0:
    total = given_list[l]
    l -= 1
print(total)



