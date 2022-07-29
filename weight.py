weight = int(input("weight"))
unit = input("(l)bs or (k)g: ")

if unit.upper() == "l":
    converted = weight * 0.45
    print(f"weight in kg: {converted}")
else:
    converted = weight // 0.45
    print(f"weight in pound:{converted}")