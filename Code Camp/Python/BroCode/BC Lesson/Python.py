# To Understand Variables and example functions for booleans in conditional statements.
#Variable types are: (1)strings, (2)integers, (3)float, and (4)booleans. ARE IN ORDER BELOW:
product = 'Laptop'
price = 180
discounted_price = 169.99
#is_student = True
#is_teacher = False

#random conditional statements for improvements in the code
evaluation = input('Are you a student or a teacher? ')
if evaluation == 'Student':
    is_student = True
    is_teacher = False
elif evaluation == 'Teacher':
    is_student = False
    is_teacher = True
else:
    print('Invalid input. Please type "Student" or "Teacher".')
    is_student = False
    is_teacher = False

#sample on Boolean prints
roles = [] #as ghost variable
if is_student:
    roles.append('a Student')
else:
    roles.append('not a Student')

if is_teacher:
    roles.append('a Teacher')
else:
    roles.append('not a Teacher')

# .join and .append are essential to put different str, on one variable, inside conditional statements.
print(f'\nYou are {' and you are '.join(roles)}.')

#This can be changed to conditional statements, which contains (if and, else) inside the curly brackets.
if is_student:
 print(f'\nYou ordered a {product} with ${price} at ${discounted_price} since you are a Student. Thank you for your purchase!')
if is_teacher:
    print(f'\nYou ordered a {product} with ${price} since you are a Teacher. Thank you for your purchase!')