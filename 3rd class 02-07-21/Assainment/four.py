#  Write a Python program to remove duplicates from a list.

list = [100,200,300,100,500,600,400,500]

dup_items = set()
uniq_items = []
for i in list:
    if i not in dup_items:
        uniq_items.append(i)
        dup_items.add(i)

print(dup_items)