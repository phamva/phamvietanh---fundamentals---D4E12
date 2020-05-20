import random
word = "champion"
a = list(word)
random.shuffle(a)
b = ' '.join(a)
print(b)
answer = input("your answer:")
if answer == word:
    print("Hura")
else:
    print(":(")
