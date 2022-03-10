#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    #game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    game = ( 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' )    
    #print(game[1:5:2])
    i = game.index('Paper')
    print(game[i])
    game.append('Computer')
    #game.insert(0, 'Computer')
    #game.remove('Paper')
    #x = game.pop(3)
    #print(x)
    #print(', '.join(game))
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
