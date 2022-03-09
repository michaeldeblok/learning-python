#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = [ 1, 2, 3, 4, 5 ]
x[4] = 42
for i in x:
    print('i is {}'.format(i))
    print(type(x))

x = range(5, 50, 5)
for i in x:
    print('i is {}'.format(i))
    print(type(x))

x = list(range(5))
x[2] = 42
for i in x:
    print('i is {}'.format(i))
    print(type(x))

x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for i in x:
    print('i is {}'.format(i))
    print(type(x))

x = { 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))
    print(type(x))


x = (1, 'two', 3.0, [4, 'four'], 5)
y = (1, 'two', 3.0, [4, 'four'], 5)


if x[0] is y[0]:
    print('yep')
else:
    print('nope')


if isinstance(x, tuple):
    print('yep')
else:
    print('nope')