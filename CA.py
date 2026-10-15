# principal = float(input("Enter principal amount: ₹"))
# rate = float(input("Enter rate of interest (%): "))
# time = float(input("Enter time (years): "))
div = int(input("Enter the div: "))


number = 1


def ca():
    principal = 1
    amount = principal * (1 + (100 / number) / 100) ** (1 * number)
    print(f"{number} Final Amount = ₹{amount}")


for i in range(div):
    ca()
    number += 1
# print(f"Compound Interest = ₹{compound_interest:.2f}")
