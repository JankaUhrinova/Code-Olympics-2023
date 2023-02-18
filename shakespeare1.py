import operator

with open("shamespeare_works.txt") as file:
    lines = file.readlines()

dictionary = {}

for line in lines:
    line = line.strip().split()
    for word in line:
        if word not in dictionary.keys():
            dictionary[word] = 0
        else:
            dictionary[word] += 1

sorted_d = dict( sorted(dictionary.items(), key=operator.itemgetter(1),reverse=True))

i = 0

for key,value in sorted_d.items():
    print(key, value)
    i += 1
    if i == 100:
        break