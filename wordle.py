import random #to generate a random word
from rich import print #allows colors in terminals to make it bonita

print("Wordle is a game where you guess the word based on given clues.")
print("CO-ORDINATION: G = wrong letter, wrong spot")
print("               Y = right letter, wrong spot")
print("               B = right letter, right spot")

#function to print on same line
def printL(a):
    print(a, end=" ")
    
#function: provides score for any given guess, handles words with repeated letters
def score(attempt, word):
    result = ["G", "G", "G", "G", "G"]
    count = {}
    
    for n, i in enumerate(attempt): #Bs, counts all letters in word
        if word[n] == attempt[n]:
             result[n] = "B"
        else:
            if word[n] not in count:
                count[word[n]] = 1
            else:
                count[word[n]] += 1
                   
    for n, i in enumerate(result): #repeated letters, all Ys
        a = attempt[n]
        if i == "B":
            pass
        elif a in count.keys():
            if count[a] > 0:
                count[a] -= 1
                result[n] = "Y"
    return "".join(result)

#function: adds color to the wordle
def color(word):
    newWord = ""
    for i in word:
        if i == "B":
            newWord += "[blue]B[/blue]"
        elif i == "G":
            newWord += "[grey62]G[/grey62]"
        elif i == "Y":
            newWord += "[gold1]Y[/gold1]"
    return "".join(newWord)
        
    
#unpacking words.txt to get the word for the code to find
n = random.randint(0, 5507)
with open("words.txt", "r") as f:
    w = [line.strip() for line in f]
    word = w[n]
    f.close()
    
#main wordle code
    
tries = 0
while tries < 6:
    attempt = input("guess? ").strip().lower()
    while len(attempt) != 5 or attempt not in w:
        attempt = input("make sure it is a valid 5-letter word! ").strip().lower()
    printL("      ")
    print(color(score(attempt, word)))
    if attempt == word: 
        print("You win!")
        break
    if tries == 5 and attempt != word:
        print(f"You lose! The word was {word}")
    tries += 1