#  Write a Python function that takes two lists and returns True if they have at least one common member.

L1 = [ 3, 5, 7, 9, 11, 13]
L2= [6,9, 10, 12, 15]

output = False

for i in L1:
    for j in L2:
        if i == j:
            output = True
print(output)