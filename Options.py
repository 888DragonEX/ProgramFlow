print("Pls choose a number representing your element:"
      "\n1.Fire\n2.Water\n3.Air\n4.Earth\n0.Quit Game")

elements=["1","2","3","4","0"]
choice=input()

while choice != "0":
    if choice in elements:
        print("Your choice of {} is invalid, pls choose another".format(choice))
    else:
        print("Pls choose a number representing your element:"
              "\n1.Fire\n2.Water\n3.Air\n4.Earth\n0.Quit Game")
    choice=input()

else:
    print("Congrats you are now the master of all elements MWAHAHA!")


# print("Please choose your option from the list below:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo swimming")
# print("4:\tHave dinner")
# print("5:\tGo to bed")
# print("0:\tExit")
# choice = "-"
#
# while True:
#     choice = input()
#     if choice == "0":
#         break
#     elif choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below:")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")
#
#     choice = input()
