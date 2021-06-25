R = float(input(" Give Your GPA: "))

if(R == 4):
    print ("Your GPA is A+")
elif(R == 3.75):
    print("Your GPA is A")
elif(R==3.5):
    print("Your GPA is A-")
elif(R==3):
    print("Your GPA is B")
elif(R==2.5):
    print("Your GPA is C")
elif(R == 2):
    print("Your GPA is D")
elif(R<2):
    print("Your GPA is F")
else:
    print("Your GPA Invalid")