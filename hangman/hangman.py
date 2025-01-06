import random
import logo
import words
print(logo.logo)

stages = logo.stages
words = words.word_list
length = len(words)
random_word = random.choice(words)
emptyList = []
for i in range(len(random_word)):
    emptyList.append("_")
print(emptyList)
print(random_word)
k = len(stages)-1
while True:
    sentence = ""
    if "_" not in emptyList:
        print("You Win")
        break
    if k <= 0:
        print("You Lose LOSER😂")
        break
    symbol = input("Guess a letter: ")
    if symbol in emptyList:
        print(f"You used letter {symbol} before")
        k-=1

    i = 0
    if symbol not in random_word:
        k = k - 1
        print("You guessed the wrong letter\n")
    while i<len(random_word):
        if symbol == random_word[i]:
            emptyList[i] = symbol




        i = i + 1
    print(emptyList)
    print(stages[k])
