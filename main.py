# import subprocess
#
#
# def speak(text):
#     subprocess.run(["termux-tts-speak", text])
#
#
# speak("Hello, welcome to Python on Termux.")

# a = int(input("enter number 1 : "))
# b = int(input("enter number 2 : "))
# print("number 1 is : ", a)
# print("number 2 is : ", b)
# print("sum of both number is : ", a + b)

# age = int(input("Enter your age : "))
# if age > 18:
#     print("You can drink bro")
# else:
#     print("you are not allowed")

# i = 2
# while i < 10:
#     print(i)
#     i += 1

# a = int(input("Enter the number for table : "))
# for i in range(1, 11):
#     print(f"{a} X {i} = {a * i}")


# def chai(n):
#     print(n)
#
#
# chai("black tea")


# from itertools import permutations
#
# # Define the digits
# digits = [1, 2, 3]
#
# # Generate all possible permutations
# result = list(permutations(digits))
#
# # Display the results
# print(result)

# from itertools import product
#
# # Define the digits
# digits = [1, 2, 3]
#
# # Generate all combinations with repetition (length of 3)
# result = list(product(digits, repeat=3))
#
# # Display the results
# print(f"Total combinations: {len(result)}")
# print(result)


# mylist.append(2)
# for item in mylist:
#     print(item)  # prints out 1,2

# import sys
#
# sys.set_int_max_str_digits(500000)
#
#
# def fac(n):
#     result = 1
#
#     for i in range(1, n + 1):
#         result *= i
#
#     return result
#
#
# print(fac(55555))


# million = 1_000_000
# total = 55_000 + 45_000  # Evaluates to 100000


# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#
#
# my_Car = Car("Toyota", "Coorola")
# print(my_Car.brand)
# print(my_Car.model)


class Book:
    def __init__(self, publication, subject) -> None:
        self.publication = publication
        self.subject = subject

    def full_name(self):
        return f'The name of your book is "{self.subject}" and it is from "{self.publication}" publication'


my_book = Book("Lucents", "General English")
print(my_book.full_name())
