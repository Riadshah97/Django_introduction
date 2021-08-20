# Concatenate two lists index-wise


list1 = ["Python", "i", "be"]
list2 = ['Django', 's', 'st']

print("The original list 1 is : " + str(list1))
print("The original list 2 is : " + str(list2))

res = [i + j for i, j in zip(list1, list2)]
print("The list after element concatenation is : " + str(res))