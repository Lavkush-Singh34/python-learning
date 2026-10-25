# Sum of natural numbers in python
# Sn = n/2{2a + (n-1) d}
# Sn = n(n-1)/2
# Sn = (n/2)(a+l)

n = int(input("enter the number to calculate sum upto this numbers : "))

# def sum_natural(n):
#     result = n * (n + 1) // 2
#     print(result)
# sum_natural(n)


# using lambda function
#
sum_natural = lambda n: n * (n + 1) // 2
print(f"ye lo answer => {sum_natural(n)}")
