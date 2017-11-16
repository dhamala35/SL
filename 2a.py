# 2. Write a python program to 
# count the frequency of words in a given file.

# Put your own path here.
fname = '/Users/apple/Desktop/Python/SL/Faid'
 
num_words = 0

with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)

print("Number of words:")
print(num_words)
