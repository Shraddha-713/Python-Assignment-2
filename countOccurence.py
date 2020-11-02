from collections import Counter
myList = [11, 45, 8, 11, 23, 45, 23, 45, 89]

for count in myList:
    dict = {
        count : Counter(myList)
    }
print(Counter(myList))
