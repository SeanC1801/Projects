# Temperature Conversion (Most complex I've ever done)
temp_input = input("Enter temperature (C or F): ").strip().lower()

# Definitions for variables
temperature = ''
unit = ''

# Extract values for variables for (1)Temperature and (2)Units
for char in temp_input:
    if char.isdigit() or char == '.' or char == '-': # If digits found then = temperature
        temperature += char
    elif char.lower() in ["c", "f", "celsius", "fahrenheit"]: # If c or f, found then = units
        unit += char

temperature = float(temperature) # Changes temp_char value to float, for conversion
unit = unit.strip() # Strips unit values from char, to be recognized in conversion.

# Validations for UNITS
if unit.lower() == "":
    print(f"Please put a valid unit")
else:
    print(f'Your temperature is {temperature}°{unit.upper()}.')

# ASK for conversion
    conversion = input("\nWould you like to convert temperature? ").strip().lower()
    if conversion.lower() in ["y", "yes", "yeah"]:
        if unit.upper() in ["C"]:
            converted = (temperature * 9) / 5 + 32
            print(f"Your converted temperature is {round(converted,3)}°F.")
        elif unit.upper() in ["F"]:
            converted = (temperature - 32) * 5 / 9
            print(f"Your converted temperature is {round(converted, 3)}°C.")

# If NO
    elif conversion.lower() in ["n", "no"]:
        input("\nPress enter to EXIT.")
    else:
        input("\nPress enter to EXIT.")
