import requests
from collections import Counter

response = requests.get("https://www.gutenberg.org/cache/epub/100/pg100.txt")
data = response.text

counter = Counter(data.lower().split())

for word, count in counter.most_common(100):
    print(word, ":", count)