# Weight converter
winput = input("Enter your weight in units (kg or lbs): ").strip().lower()

# Definition for variable
weight = ""
unit = ""

# Extract variable
for char in winput:
    if char.isdigit() or char == '.' or char == "-":
        weight += char
    elif char.lower() in ["k", "l", "kg", "lbs"]:
        unit += char

weight = float(weight)
unit = unit.strip()

# Validations for Unit with Random Weight Management Advice
if unit.lower() == "":
    print(f"\nPlease enter your weight in a valid unit (K or L)")
else:
    if unit.lower() in ["k", "kilograms", "kg"]:
        print(f"Your weight is {round(weight,3)}kgs.")
        if weight >= 100:
            print("Can't you go on a diet?")
        elif weight <= 30:
            print("Are you malnourished? Go eat some food.")
    elif unit.lower() in ["l", "lbs", "lbs"]:
        print(f"Your weight is {round(weight,3)}lbs.")
        if weight >= 220:
            print("Can't you go on a diet?")
        elif weight <= 65:
            print("Are you malnourished? Go eat some food.")

# Conversion
    conversion = input("\nWould you like to convert weight?: ")
    if conversion.lower() in ["y", "yes"]:
        if unit.lower() in ["k", "kilograms", "kg"]:
            weight *= 2.2046
            print(f"Your converted weight is {round(weight, 3)}lbs.")
        elif unit.lower() in ["l", "pounds", "lbs"]:
            weight /= 2.2046
            print(f"Your converted weight is {round(weight, 3)}kg.")
    elif conversion.lower() in ["n", "no"]:
        input("Press ENTER to exit.")
    else:
        input("Press ENTER to exit.")

