age= int(input("What is your age?"))
if age>=16 and age<=65:
    print("Another day at work :< ")
else:
    print("I dont have to work yay!")
print("-" * 80)

if 16 <=age<= 65:
    print("Another day at work :< ")

if 65>= age >= 16:
    print("Another day at work :< ")
print("-" * 80)

if age<16 or age>65:
    print("I dont have to work yay!")
else:
    print("Another day at work :< ")
