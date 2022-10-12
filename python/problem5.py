print("Become the programmer you're meant to be!")



# find whther string of dierections lead him to direction where he started
direction_string=input()
east_count=direction_string.count("E")
west_count=direction_string.count("W")
north_count=direction_string.count("N")
south_count=direction_string.count("S")


if (east_count==west_count==north_count==south_count):
    print("ok")
else:
    print("not ok")