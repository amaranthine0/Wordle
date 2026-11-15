import random #to generate a random word
from rich import print #allows colors in terminals to make it bonita
import json #to save the stats locally for each person
import os #to check whether the stats file already exists or not

#function to print on same line
def printL(a):
    print(a, end=" ")
    
#function: provides score for any given guess, handles words with repeated letters
def score(attempt, word):
    attempt = attempt.strip().lower()
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

#function: loads player stats after a game
def load_stats(): 
    if os.path.exists("stats.json"):
        with open("stats.json", "r") as f:
            return json.load(f)
    else:
        return {
            "played": 0,
            "wins": 0,
            "streak": 0,
            "maxStreak": 0,
            "winRate" : 0,
            "dist" : {"1" : 0, "2" : 0, "3": 0, "4" : 0, "5" : 0, "6" : 0}
            #NOTE: dictionaries in json only allow string keys
            #      python allows for int keys :p
        }

#function: saves player stats after a game
def save_stats(stats):
    with open("stats.json", "w") as f:
        json.dump(stats, f)

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
        
def main():
    stats = load_stats()
    print("Wordle is a game where you guess the word based on given clues.")
    print("CO-ORDINATION: G = wrong letter, wrong spot")
    print("               Y = right letter, wrong spot")
    print("               B = right letter, right spot")

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
            stats["played"] += 1
            stats["wins"] += 1
            stats["streak"] += 1
            if stats["streak"] > stats["maxStreak"]:
                stats["maxStreak"] = stats["streak"]
            stats["dist"][str(tries + 1)] += 1
            stats["winRate"] = int((stats["wins"] / stats["played"]) * 100)
            print("You win!")
            break
        if tries == 5 and attempt != word:
            stats["played"] += 1
            stats["streak"] = 0
            stats["winRate"] = int((stats["wins"] / stats["played"]) * 100)
            print(f"You lose! The word was {word}")
        tries += 1
    save_stats(stats)
    
    print()
    print(f"PLAYED : {stats["played"]}")
    print(f"WINS : {stats["wins"]}")
    print(f"STREAK : {stats["streak"]}")
    print(f"MAX STREAK : {stats["maxStreak"]}")
    print(f"WIN RATE : {stats["winRate"]}%")
    print("WINS IN GUESSES")
    for i in range(1, 7):
        print(f"{i} : {stats["dist"][str(i)]}")
        
if __name__ == "__main__":
    main()