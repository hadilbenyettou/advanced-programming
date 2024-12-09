str = input("please type in a string : ")
frame_width = 30
space_c = (frame_width - len(str)) // 2 - 1

print(
    "*" * frame_width
    + "\n"
    + "*"
    + " " * space_c
    + str
    + " " * (frame_width - len(str) - space_c - 2)
    + "*"
    + "\n"
    + "*" * frame_width
)
