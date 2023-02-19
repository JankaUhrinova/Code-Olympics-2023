import requests
from collections import Counter

def ngram(s, n):
    if n < 1: return []
    return [tuple(s[i:i+n]) for i in range(len(s)-n+1)]

response = requests.get("https://www.gutenberg.org/cache/epub/100/pg100.txt")
words = response.text.lower().split()
word_grams = [ngram(words, n) for n in range(6)]

for i in range(2,6):
    counter = Counter(word_grams[i])
    print(counter.most_common(10))