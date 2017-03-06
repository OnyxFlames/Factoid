import random

PHRASES = [
    "sudo rm -rf /", "/dev/null", "Try constructing additional pylons?",
    "BorKeD", "If you're seeing this message: something goofed!",
    "Yikes! That page doesn't exist.",
    "We Factoid! up somewhere.", "I think my server is on fire.",
    "Despite popular belief: Computers infact do NOT like to go swimming."]

def getRandomPhrase():
    return PHRASES[random.randint(0, len(PHRASES)-1)]