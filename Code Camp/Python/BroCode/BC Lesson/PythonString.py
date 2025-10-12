# Python String Basics to search and manipulate a string.

name = input('What is your name? ') # bro Code
contact = '1-092-333-2034'

print("\nString Basics:")

# To identify and locate variables
print(f'Name Length: {len(name)}') # len - to measure the length of an input
print(f'Number of Dashes: {contact.count('-')}') # To count a specific input
print(f'"O" located (Beginning): {name.find("o")}') # .find - to search an occurrence from the beginning
print(f'"O" located (Ending): {name.rfind("o")}') # .rfind - to search an occurrence first from the last

# Letter Manipulation
print(f'\nCapitalization: {name.capitalize()}') # Capitalizes, first letter
print(f'In All Upper Case: {name.upper()}') # Upper case on all letters
print(f'In All Lower Case: {name.lower()}') # Lower case on all letters
print(contact.replace('-', ' '))

# Boolean Statements
number = '123'
letter = 'Abc'
print(f'\nName in digits: {name.isdigit()}') # False since there is no digit found
print(f'Digit in digits: {number.isdigit()}') # True since there are digits found
print(f'Letters in alphabetic: {letter.isalpha()}') # Boolean to identify if statement is an alphabet