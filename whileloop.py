# i=1
# while i<5:
#     print("i={}".format(i))
#     i+=1

# while True:
#     print ("gg.com")
#     print("mega gg.com")
#     break

available_exits = ["north", "south", "east", "west"]

chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold()=="quit":
        print("Game over")
        break
    elif chosen_exit.casefold() in available_exits:
        print("aren't you glad you got out of there")
    else:
        continue

for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
      break

