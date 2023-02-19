import random

dinosaurs = {
    "Argentinosaurus" : 128,
    "Brachiosaurus" : 85,
    "Barosaurus" : 79,
    "Tyrannosaurus rex" : 39,
    "Triceratops" : 30,
    "Chicken" : 2.3,
}

fact = {
    "Argentinosaurus" : "Argentinosaurus was a truly massive dinosaur.",
    "Brachiosaurus" : "The largest dinosaur known from a relatively complete fossilized skeleton.",
    "Barosaurus" : "Scientists have yet to discover a Barosaurus skull.",
    "Tyrannosaurus rex" : "T. rex was quite smart, boasting a brain twice as big as those of the other giant carnivores.",
    "Triceratops" : "Some Triceraptors had as many as 800 teeth!",
    "Chickens" : "They might have evolved either before the egg or after the egg.",
}

dino_list=["Argentinosaurus", "Brachiosaurus", "Barosaurus", "Tyrannosaurus rex", "Triceratops", "Chicken"]

size = int(input("Give us the size in feet you wish to compare: "))
dino = random.choice(dino_list)

print( f'{size}ft is {size/dinosaurs[dino]} of the size of a {dino}.')
print( f'Fun fact about {dino}:')
print(fact[dino])


