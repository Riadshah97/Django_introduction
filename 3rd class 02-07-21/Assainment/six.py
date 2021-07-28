
# create custom count function.

List = ['x','y','z','x','x','x','y','z']
count = 0
for i in List:
    if i == 'x':
        count += 1
print("Custom Output:", count)