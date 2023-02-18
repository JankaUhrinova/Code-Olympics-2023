with open("keylog.txt") as file:
    lines = file.readlines()
lines = set(lines)
numbers = [0]*10
print(numbers)
for line in lines:
    line = line.strip()
    pos = -1
    for l in line:
        numbers[int(l)] = numbers[int(l)] + pos
        pos +=1

for i in range(10):
    print(i,"is at somewhere around", numbers[i])