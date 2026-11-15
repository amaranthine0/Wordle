#this file is just for me to understand how testing works within a dev setup and try it out
from wordle import score

def testWordle(attempt, word, result):
    return score(attempt, word) == result

tests = [
    testWordle("crANe", "crane", "BBBBB"),
    testWordle("ghost", "crane", "GGGGG"),
    testWordle("speed  ", "abide", "GGYGY"),
    testWordle("eerie", "abide", "GGGYB"),
    testWordle("gEEse", "elder", "GYYGG"),
    testWordle("llama", "hello", "YYGGG"),
    testWordle("hello", "llama", "GGYYG"),
    testWordle("APPLE", "paper", "YYBGY"),
    testWordle("civic", "cycle", "BGGGY"),
    testWordle("sassy", "asset", "YYBGG")
]

print(tests)