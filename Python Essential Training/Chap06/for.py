#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    print(pet)

    if pet == 'dog': continue
    if pet == 'velociraptor': break
    print(pet)

else:
    print('that is all of the animals')