#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# def main():
#     print('Hello, World.')



def f1(f):
    def f2():
        print('this is before a function call')
        f()
        print('this is after a function call')
    return f2
    #print('this is f1')

def f3():
    print('this is f3')


# x = f1(f3)
# x()

# f3 = f1(f3)
# f3()

@f1
def f3():
    print('this is f3')

f3()



# if __name__ == '__main__': main()
