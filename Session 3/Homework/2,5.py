List = [10,20,30,40,50,60,70,80]
print("hello", "," , "my name is VA and these are my ship size")
print(List)
print("Month 1:")
print('1 month has passed , now here my flock')
newlist = [value + 50 for value in List]
print(newlist)
a = max(newlist)
print("now my biggest sheep has size ", a , "let's shear it")
print("after shearing , here is my flock")
number = newlist.index(a)
newlist[number] = 8
print(newlist)

print("-------")

print("Month 2:")
print('2 month has passed , now here my flock')
newlist2 = [value + 50 for value in newlist]
print(newlist2)
b = max(newlist2)
print("now my biggest sheep has size ", b , "let's shear it")
print("after shearing , here is my flock")
number2 = newlist2.index(b)
newlist2[number2] = 8
print(newlist2)

print("-------")

print("Month 3:")
print('3 month has passed , now here my flock')
newlist3 = [value + 50 for value in newlist2]
print(newlist3)
c = max(newlist3)
print("now my biggest sheep has size ", c , "let's shear it")
print("after shearing , here is my flock")
number3 = newlist3.index(c)
newlist3[number3] = 8
print(newlist3)
