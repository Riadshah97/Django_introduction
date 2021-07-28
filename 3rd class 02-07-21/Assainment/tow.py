# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. Go to the editor

str1 = input("enter the value :")

str2=str1

str3=str4=0

str3 = str1.find('not')
str4 = str1.find('poor')

if(str3>=0 and str4>=0):
    str2 = str2.replace(str2[str3:str4+4],'good')
    print(str2)