# key value pair
dic ={
    "key1":"value1",
    "key2":"value2",
    "key3": "value3"
}
print(dic)
print(type(dic))
print(dic['key1'],dic['key2'])

for i,j in dic.items():
    print(i,j)

dic={
     "name" : "Riad",
     "age": 23,
      "address": {
       "present": "Mirpur,dhaka",
         "permanent":{
          "House1": "mithapukur,Rangpur",
            "House2": "USA",

        }
      }
 }
print(dic['name'], dic['address']['permanent']['House2'])

df={
    "Name": ["Riad", "Rafi", "Hasib", "topu"],
    "deft": ["CSE", "EEE", "IT", "ENG"],
    "semester": ["2nd", "3rd", "5th", "6th"],
}
for i,j in df.items():
 print(i,j)

 print(df.values())
 print(df.keys())
 print(df.get("Name"))
 print(df.update())