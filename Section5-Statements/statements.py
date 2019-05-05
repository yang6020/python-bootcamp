# if else
num1 = 1
num2 = 2
bool1 = True
if bool1:
    num1 = 2
else:
    num1 = 0
print('if else', num1 + num2)

# for
arr = [1, 2, 3, 4]
acc = 0
for num in arr:
    acc += num
print('for',acc)

# while
countDown = 5
acc = 0
while countDown != 0:
    acc += 1
    countDown -= 1
print('while', acc)

# break - break out of current loop
arr = ["J", "U", "S", "T", "I", "N"]
for letter in arr:
    if letter == "U":
        break
    print("break", letter)

# continue - goes to the top of the enclosing loop
arr = ["J", "U", "S", "T", "I", "N"]
for letter in arr:
    if letter == "U":
        continue
    print('cont', letter)

# pass - do nothing
for num in arr:
    pass
print("end of script")

