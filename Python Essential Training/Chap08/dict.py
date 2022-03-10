#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = dict(kitten = 'meow', puppy = 'ruff!', lion = 'grrr', giraffe = 'I am a giraffe!', dragon = 'rawrr')
    #animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr', 'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    # for k, v in animals.items():
    #     print(f'{k}: {v}')
    print_dict(animals)

def print_dict(o):
    for k, v in o.items(): print(f'{k}: {v}')

    #for x in o: print(f'{x}: {o[x]}')

if __name__ == '__main__': main()
