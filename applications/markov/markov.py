import random


# Read in all the words in one go
with open("/Users/lesley/code/Python/Projects/cs-module-project-hash-tables/applications/markov/input.txt", "r") as f:
    words = f.read()

split = words.split()
dictionary = {}

next = None

for word in split:
    if word not in dictionary:
        dictionary[word] = []

for i in range(len(split)-1):
    current_word = split[i]
    dictionary[current_word].append(split[i + 1])
# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here
