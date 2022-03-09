#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quaaaack!'
    walking = 'Walks like a duck.'

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()

print("")
print("")
print("")


class Tree:
    height=5
    def Height(self):
        print('height is {}'.format(self.Height))
Elm=Tree()
Elm.Height()