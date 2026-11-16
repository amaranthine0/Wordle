#a simple wordle solver bot using words.txt
from wordle import score
from wordle import color 
from rich import print #allows colors in terminals to make it bonita
import random #randomly choose a word
       
#function: filters out such that only possible solutions remain                 
def filter_candidates(words ,guess, result):
    #uses inverse functions concept [hardest part to code]
    newWords = []
    for j in words:
        if score(guess, j) == result:
            newWords.append(j)
    return newWords

#function: chooses a random next word to guess
def pick_guess(candidates, guessCount):
    if guessCount == 1:
        return "adieu"
    else:
        return random.choice(candidates)
    
#function: the bot plays :p
def bot_play(ans, words):
    guess = 1
    while guess < 7:
        newWord = pick_guess(words, guess)
        newVal = score(newWord, ans)
        print(guess, newWord, color(newVal), len(words))
        if newVal == "BBBBB":
            return guess
        else:
            words = filter_candidates(words, newWord, newVal)
        guess += 1
    return 0

def main():
    #unpacking words.txt to get the word for the code to find
    n = random.randint(0, 5507)
    with open("words.txt", "r") as f:
        w = [line.strip() for line in f]
        word = w[n]
        f.close()
    
    print(bot_play(word, w))
    
if __name__ == "__main__":
    main()