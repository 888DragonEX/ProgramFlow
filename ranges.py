# for i in range (10,15):
#     print("i is now {}".format(i))
#
# print()
#
# for i in (10,15):
#     print("i is now {}".format(i))

# for i in range (10,0,-2):
#     print("i is now {}".format(i))


# Print all numbers from 0 to 100 that are divisible by 7
# and also numbers containing 7:

for i in range(0,101):
    if i%7==0 or i in range(7,101,10) or i in range(70,80):
        print(i)

