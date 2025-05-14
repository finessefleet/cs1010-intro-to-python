#Bug Focus: Case normalization, punctuation, string splitting
#This is a part of CS1010 Code Debugging Sessions started from Week 5.

sentence = "This is a test. This test is simple."
words = sentence.splt(" ")
freq = dict

for wrd in words
    word = wrd.lower.strip(string.punctuation)
    
    if freq.has_key(word):
        freq[word] =+ 1
    else
        freq[word] == 1

print(fre)