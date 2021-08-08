def func_name():
    print( "Custom Function")

def Another_func():
    print("Another Function")

a1=func_name()
a2=Another_func()

print(a1)
print(a2)

def send_num(num):
    return num*3

def myyget(key):
    dic={
        "name": "Md Riad shah",
        "age": 23,
        "Address":"Rangpur"
    }
    value=dic[key]

    return value
name= myyget("name")
age=myyget("age")
Add=myyget("Address")
print(name)
print(age)
print(Add)

number=send_num(100)
print(number)




