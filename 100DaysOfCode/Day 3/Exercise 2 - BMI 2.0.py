# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

result = weight / (height ** 2)
BMI = round(weight / (height ** 2))


if result <= 18.5:
    print(f'Your BMI is {BMI}, you are underweight')
elif result <= 25:
    print(f'Your BMI is {BMI}, you have a normal weight.')
elif result <= 30:
    print(f'Your BMI is {BMI}, you are slightly overweight.')
elif result <= 35:
    print(f'Your BMI is {BMI}, you are obese.')
elif result > 35:
    print(f'Your BMI is {BMI}, you are clinically obese.')
