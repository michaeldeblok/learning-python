# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

#print(sum(student_heights))

def get_number_of_elements(student_heights):
    count = 0
    for element in student_heights:
        count += 1
    return count

#print("Number of elements in the list: ", get_number_of_elements(student_heights))

print(round(sum(student_heights) / get_number_of_elements(student_heights)))


total_height = 0
for height in student_heights:
  total_height += height
print(f"total height = {total_height}")

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(f"number of students = {number_of_students}")
  
average_height = round(total_height / number_of_students)
print(average_height)

