#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from functools import update_wrapper


print('Hello, World.')
print('Hello, World.'.upper())
print('Hello, World.'.lower())
print('Hello, World.'.capitalize())
print('Hello, World.'.title())
print('Hello, World.'.swapcase())
print('Hello, World.'.casefold())
# print('Hello, World.'.count())
# print('Hello, World.'.center())
print('')
s1 = 'Hello, World.'
s2 = 'This is another string'

print (s1 + ' ' + s2)

print('')
print('')

x = 42
y = 73
print('the number is {}'.format(x, y))
print('the number is {} {}'.format(x, y))
print('the number is {xx} {bb}'.format(xx = x, bb = y))
print('the number is {0} {1} {0}'.format(x, y))
print(f'the number is {x}')
print('the number is {0:<5} {1:>05}'.format(x, y))
print('the number is {0:<5} {1:>+05}'.format(x, y))


x = 42 * 747
print('the number is {:,}'.format(x))
print('the number is {:,}'.format(x).replace(',', '.'))
print('the number is {:f}'.format(x))
print('the number is {:.3f}'.format(x))
print('the number is {:x}'.format(x))
print('the number is {:o}'.format(x))
print('the number is {:b}'.format(x))
print(f'the number is {x:.3f}')
