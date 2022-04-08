# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#     print('Hello Michael')
#     print('How do you do Jack Bauer?')
#     print('Isn\'t the weather nice today?')

# greet()

# print('\n\n')

# def greet_with_name(name):
#     print(f'Hello {name}')
#     print(f'How do you do {name}?')

# greet_with_name('Michael')


def greet_with_name(name, location):
    print(f'Hello {name}')
    print(f'How do you do {name}?')
    print(f'How is the weather in {location}? ')

greet_with_name(name='Michael',location='Amsterdam')
