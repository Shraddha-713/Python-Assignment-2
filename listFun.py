myList = [87, 45, 41, 65, 94, 41, 99, 94]
print("Sample List- ", myList)
myNewList = list(dict.fromkeys(myList))
print("Unique Items- ",myNewList)
myTuple = tuple(myNewList)
print("Tuple= ", myTuple)
print("Min- ", min(myNewList))
print("Max- ", max(myNewList))
