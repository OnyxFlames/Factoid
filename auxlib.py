import random

phrases = [
    "sudo rm -rf /", "Try constructing additional pylons?",
    "BorKeD",  "If you're seeing this message: something goofed!", " Yikes! That page doesn't exist.",
    "We Factoid! up somewhere."]

def getRandomPhrase():
    return phrases[random.randint(0, len(phrases)-1)]