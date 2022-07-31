import math
room = input()
numSet = 0

if "9" or "6" in room:
    a = room.count("9") + room.count("6")
    numSet = math.ceil(a/2)

for i in range(len(room)):
    if room.count(room[i:i+1]) > numSet:
        if room[i:i+1] == "9" or room[i:i+1] == "6":
            continue
        numSet = room.count(room[i:i+1])
print(numSet)        