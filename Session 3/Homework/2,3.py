List = [10,20,30,40,50,60,70,80]
print("hello", "," , "my name is VA and these are my ship size")
print(List)
a = max(List)
print("now my biggest sheep has size ", a , "let's shear it")
number = List.index(a)
List[number] = 8
print("after shearing , here is my flock")
print(List)