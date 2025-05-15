#dictionary constructor should be called
#nameError in split()
#has.key() is removed from py3
#lower should be called lower()
#short hand operator in if body should be +=

import string

sentence = "This is a test. This test is simple."
words = sentence.split(" ")
freq = dict()

for wrd in words:
    word = wrd.lower().strip(string.punctuation)
    
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
