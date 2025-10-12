# Weight Converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit.lower() in ["k", "kilograms", "kg"]:
    print(f'Your weight is {weight} kg.')
elif unit.lower() in ["l", "pounds", "lbs"]:
    print(f'Your weight is {weight} lbs.')
else:
    print('You must enter K or L for your unit.')

conversion = input("\nWould you like to convert your weight? ")

if conversion.lower() in ["yes", "y"]:
 if unit.lower() in ["k", "kilograms", "kg"]:
    weight *= 2.2046
    print(f"Your converted weight is {round(weight,3)}lbs.")
 elif unit.lower() in ["l", "pounds", "lbs"]:
    weight /= 2.2046
    print(f"Your converted weight is {round(weight, 3)}kg.")

elif conversion.lower() in ["no" or "n"]:
    input("Press ENTER to exit.")
else:
    input("Press ENTER to exit.")