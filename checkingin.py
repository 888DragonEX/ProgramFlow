name= input("What is your name?")
age= int(input("How old are you?"))
if 18< age< 31:
    print("Welcome aboard!")
else:
    print("Sorry but you don't meet the requirements :<")

---------------------------------

dragon= "fire breathing"
learn= input("I want to learn: ")

if learn.casefold() not in dragon:
    print("{} is not part of {}".format(learn,dragon))
else:
    print("Congrats you've learnt it!")

    #letter= input("Enter a character: ")
# if (letter in dragon):
#     print("{} is in {}".format(letter,dragon))
# else:
#     print("I dont need that letter")