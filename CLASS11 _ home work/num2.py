# Given a range of the first 10 numbers, Iterate from the start number to the end number, and In each iteration
#  print the sum of the current number and previous number

sum = 0
for i in range(10):
    prev = sum
    sum += i
    print("Current Number:", i, "Previous number :", prev, "Sum:", sum)
