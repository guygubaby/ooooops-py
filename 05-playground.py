def word_length(phrase):
  return list(map(lambda word: len(word),phrase.split(' ')))


lst = word_length('How long are the words in this phrase')

print(lst)
