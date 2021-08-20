#  Accept number from user and calculate the sum of all number from 1 to a given number

n = int(input("Enter the number"))
sum = 0
for i in range(1, n + 1, 1):
    sum = sum + i
print("Sum of first ", n, "numbers is: ", sum)