#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random

def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))

    v = sys.platform
    print(v)

    print()

    v = os.name
    print(v)

    print()

    v = os.getenv('PATH')
    print(v)

    print()

    v = os.getcwd()
    print(v)

    print()

    v = os.urandom(25).hex()
    print(v)
    
    print()

    x = random.randint(1, 1000)
    print(x)

    x = list(range(25))
    print(x)
    random.shuffle(x)

if __name__ == '__main__': main()
