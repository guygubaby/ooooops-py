from collections import Counter


phrase = 'How many times does each word show up in this sentence word times each each word'

wrods = phrase.split()

c = Counter(wrods)

print(c.elements())
print(c.most_common(3))