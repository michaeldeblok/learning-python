#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = 112
    print('x < y: x is {} and y is {}'.format(x, y))
    print("Line 2")
    print("Line 3")
    print("Line 4")
elif x > y:
    print('x < y: x is {} and y is {}'.format(x, y))
else:
    print("do something else")

print("z is {}".format(z))
print(f"z is {z}")

