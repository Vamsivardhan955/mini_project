import random
print("WELCOME TO HANGMAN")
heart=6
won=False
list1= ["lamp", "chair", "book", "spoon", "tree", "hat", "bike", "door", "pen", "cup", "shoe", "clock", "ball", "table", "sun", "moon", "flower", "bridge", "cloud", "pillow"]
# random words
word=random.choice(list1)#choose a random word from the list
word=list(word)#make it in to list again
output = ["_"] * len(word)
print(output)
while heart:
    guess=input("Guess a letter:")
    for i in range(len(word)):
        if(guess==word[i]):
            output[i]=guess
            print(output)
            if(output==word):
                won=True
                print("you won!")

    if (guess not in word):
                    heart -= 1
                    print(f"You have {heart} heart left")
    if(won==True):
        break
    if(heart==0):
        print(f"The word is {word}")

