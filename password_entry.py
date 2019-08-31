date_input = input("Enter DOB (d/m/y)")
parts = date_input.split("/")
my_dob = tuple([int(part) for part in parts])

print(my_dob)

