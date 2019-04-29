# Numbers
testNumber = 100
print(type(testNumber))

testNumber = testNumber * 10
print(testNumber)
print(testNumber % 10)
print(testNumber - 100)

# Strings
myString = "hello"
print(myString[-1] == "o")
print(myString[::-1])

yellow = myString[1:]
yellow = "Y" + yellow
print(yellow)
print(yellow.upper())
print(yellow.lower())

yellowArray = list(yellow)
print(yellowArray)
print("{} world".format(myString))
print(f"{myString} world")
print("{a} {b} {c}".format(a="the", b="quick", c="brown"))

# Arrays & Tuples & Sets

numArr = [4, 2, 3, 1]
strArr = ["d", "a", "c", "b"]
numArr.sort()
print(numArr)
numArr.reverse()
print(numArr)

numTupple = (4, 2, 3, 1)
strTupple = ("a", "b", "d", "c")
print(type(numTupple))

# Tuples are immutable!
try:
    numTupple[0] = 5
except TypeError:
    print(TypeError)

# Sets are unique
numArr = [4, 4, 3, 1]
numSet = set(numArr)
print(numSet)

# Dictionaries
myDict = {"key": "value"}
print(myDict["key"])
myDict["key2"] = 2
print(myDict)
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict["key"])

# Files and IO
myfile = open("./test.txt")
print(myfile.read())

# Think of reading as a cursor, when you read the file, it reads till the end. If you call
# .read again, it will return ''
print(f"it returns {myfile.read()}")

# To reset the cursor, you need to seek 0, readlines will give you an array based on lines
myfile.seek(0)
contents = myfile.readlines()
print(contents)

# Usually, when reading the file, close the file after. You can do it like below.
# Using with closes the files automatically after
# modes
# w = write
# r = read
# a = append
# r+ = read + write
# w+ = Overwrite existing file / create a new file

with open("./test.txt", mode="r") as newFile:
    print(newFile.read())

with open("./test.txt", "a") as newFile:
    newFile.write("\nthis is the sixth line")

with open("./test.txt", "r") as newFile:
    print(newFile.read())

