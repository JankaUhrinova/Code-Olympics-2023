with open("keylog.txt") as file:
    lines = file.readlines()
lines = set(lines)
numbers = [0]*10
for line in lines:
    line = line.strip()
    pos = -1
    for l in line:
        numbers[int(l)] = numbers[int(l)] + pos
        pos +=1

password = []
for i in range(10):
    print(i,"is at somewhere around", numbers[i])
    password.append((numbers[i],i))

zero = True
result = ""

for t in sorted(password):
    if t[0] == 0:
        if zero:
            result += str(t[1])
            zero = False
    else:
        result += str(t[1])

print("The password is:", result)