a = 15
b = 9

c = 2
d = 3
#Arithmetic Operators
result1 = a+b
result2 = a-b
result3 = a*b
result4 = a%b
result5 = a/b
result6 = a//b
result7 = c**d

print('Sum := ',result1)
print('Diff := ', result2)
print('Product := ',result3)
print('Quotient := ',result4)
print('Division := ', result5)
print('Floor Division := ',result6)
print('Exponent := ',result7)

#Logical and Identity Operators
print(a is b)
print(a is not b)

print(a is b and a is not b)
print(a is not b and a is not b)
print(a is b or a is not b)
print(not (a!=b))
print (a!=b)

#Comparison Operators
if a==b:
    print('a and b are same')
elif a!=b:
    print('a is not equal to b')
    if a>b:
        print('a is greater than b')
    elif a<b:
        print('a is lesser than b')

#Membership Operators 

my_list =["1","2","3","4","5"]
result8 = "1" in my_list
print(result8)

result9 = "8" not in my_list
print(result9)


