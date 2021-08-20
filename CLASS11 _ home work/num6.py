#  Reverse the following list using for loop

digits = [10, 20, 50, 70, 100]

for i in range(len(digits)):
     last_item = digits.pop()
     digits.insert(i, last_item)
     print(digits[i])