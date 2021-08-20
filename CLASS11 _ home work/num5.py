# Given a list, iterate it, and display numbers divisible by five,
# and if you find a number greater than 150, stop the loop iteration.

My_list = [10, 17, 28, 40, 60, 90, 124, 150, 180, 290]
for i in My_list:
    if (i > 150):
        break
    if(i % 5 == 0):
        print(i)