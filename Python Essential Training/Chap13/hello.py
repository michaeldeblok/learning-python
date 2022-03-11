#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

x = ( 1, 2, 3, 4 , 5)
y = ( 6, 7, 8, 9, 10 )
z = zip(x, y)

for a, b in z: print(f'{a} - {b}')

x = ( 'cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x): print(f'{i}: {v}')

# i = index
# v = value

# https://docs.python.org/3/library/functions.html

print()
print()
print()

x = 42
y = type(x)
print(x)
print(y)

x=abs(int(float(-4.5+3.2)))
print(x-1j)