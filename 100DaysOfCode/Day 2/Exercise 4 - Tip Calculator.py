#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!\n")

bill = int(input('How much was the total bill? '))
people = int(input('Between how many people would you like to split the bill? '))
tip = int(input('How much of a tip would you like to give? [Popular tips = 15% / 18% / 20%] '))

total = round(bill * (1 + tip/100), 2)
share = round(total / people, 2)

print(f'\nEach person should pay ${share}, resulting in a total of ${total}.')
