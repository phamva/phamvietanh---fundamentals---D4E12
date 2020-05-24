x,y = 1,2

print("month 0 :" , x , "pair(s) of rabbit")
print("month 1 :" , y , "pair(s) of rabbit")
while y<8:
   a = x + 1
   x,y = y,y+x
   print("month", a,":" , y , "pair(s) of rabbit")

