def calculate_hypotenuse(a, b):
    return (a**2 + b**2)**0.5

def calculate_leg(c, a):
    return (c**2 - a**2)**0.5

# Main program
print("Pythagorean Theorem Calculator")

# Option to calculate the hypotenuse
a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
c = calculate_hypotenuse(a, b)
print(f"The length of the hypotenuse is: {c:.2f}")

# Option to calculate a leg if hypotenuse and the other leg are known
c = float(input("Enter the length of the hypotenuse 'c': "))
a = float(input("Enter the length of one leg 'a': "))
leg = calculate_leg(c, a)
print(f"The length of the other leg is: {leg:.2f}")
