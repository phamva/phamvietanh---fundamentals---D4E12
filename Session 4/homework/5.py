price = {
    "banana" : 4 ,
    "apple" : 2 ,
    "orange" : 1.5 , 
    "pear" : 3
}

stock = {
    "banana" : 6 ,
    "apple" : 0 , 
    "orange" :32 ,
    "pear" : 15 ,
}

for key in price :
    x = (price.get(key))
    y = (stock.get(key))
    print(key , "\n" , "price", x , "\n" , "stock" , y)
    new_price = x*y
    print(new_price)
    print("newtotal =" , new_price)



