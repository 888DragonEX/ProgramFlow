# dragon= "flame"
#
# for powers in dragon:
#     print(powers)

numbers= "957^3_792^10"
separators=""

for x in numbers:
    if not x.isnumeric():
        separators= separators + x
    print(separators)

