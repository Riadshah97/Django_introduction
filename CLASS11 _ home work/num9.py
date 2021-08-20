# Given a Python list of numbers. Turn every item of a list into its square

numbers = [3, 5, 7, 9, 10]

squaring_iterator = map(lambda n: n ** 2, numbers)
squared_numbers = list(squaring_iterator)

print(squared_numbers)