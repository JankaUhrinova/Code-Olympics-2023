def stage1(prompt, buttons, pstages):
    position = [None, 2, 2, 3, 4][prompt]
    return position, buttons[position]

def stage2(prompt, buttons, pstages):
    position = None
    if prompt == 1:
        position = buttons.index(4)
    if prompt in (2, 4):
        position = pstages[1][0]
    if prompt == 3:
        position = 1
    return position, buttons[position]

def stage3(prompt, buttons, pstages):
    position = None
    if prompt == 1:
        label = pstages[2][1]
        position = buttons.index(label)
    if prompt == 2:
        label = pstages[1][1]
        position = buttons.index(label)
    if prompt == 3:
        position = 3
    if prompt == 4:
        position = buttons.index(4)
    return position, buttons[position]

def stage4(prompt, buttons, pstages):
    position = None
    if prompt == 1:
        position = pstages[1][0]
    if prompt == 2:
        position = 1
    if prompt in (3, 4):
        position = pstages[2][0]
    return position, buttons[position]

def stage5(prompt, buttons, pstages):
    position = pstages[prompt][0]
    return position, buttons[position]

def parse_text_array(text):
    text = "".join(text.splitlines())
    rows = text.replace("[", "").split("]")
    array = [[x.strip() for x in line.split(",")] for line in rows]
    array = [[x for x in line if x] for line in array]
    array = [line for line in array if line]
    array = [[int(x) for x in line] for line in array]
    return array

def parse_instructions(array):
    return [([None] + day[:-1], day[-1]) for day in array]

import sys
text = sys.stdin.read()
array = parse_text_array(text)
# print(*array, sep="\n")
days = parse_instructions(array)
# print(*days, sep="\n")

stages = [stage1, stage2, stage3, stage4, stage5]
pstages = [(None, None)]
for stage, (buttons, prompt) in zip(stages, days):
    position, label = stage(prompt, buttons, pstages)
    pstages.append((position, label))

password = "".join([str(label) for _, label in pstages[1:]])
print(password)