# list, tuple, set, dictionary
#index = 0-> n-1
l = [1,2,3,4.5,5.5,6.5,"seven","eight","nine"]

print(l[4])
print(type(l[4]))
print(type(l))
print(l)

l.append("ten")
print(l)

l.insert(4, 10)
print(l)

print(l.index("nine"))

print(l.count(5.5))

print(l.pop())
print(l)
print(l.pop(0))
print(l)

l=[3, 4, 5, 2, 1, 14, 23, 8, 10, 9]
print("Before sorting",l)
l.sort()
print("After sorting",l)

l.reverse()
print(l)

l.remove(14)
print(l)

#Nasted list

l=[[1,2,[3.1,3.2,3.3]],[4,5,6],[7,8,9]]
print(l[0][1])
print(l[0][2][2])

#mutable,imutable
l[0]=100
print(l)

print("#"*50)
#tuple
t=[1,2,3,4,5,6]
print(t)




#for i in l:

 #   print(type(i))
  #  print(i)