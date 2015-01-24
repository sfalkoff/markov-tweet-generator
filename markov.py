#!/usr/bin/env python

import sys
import random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    text_file = open(corpus)
    w = text_file.read().rstrip().split()
    chains_dict = {}
    
    for i in range(len(w) - 2):
        key = (w[i], w[i + 1])
        value = w[i + 2]
        
        if key in chains_dict:
            chains_dict[key].append(value)
        else:
            chains_dict[key] = [value]
        #No longer in use, kindof cool: chains_dict[tuple(text_file[i : i + 2])] = list([text_file[i + 2]])

    text_file.close()
    return chains_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    random_w = []
    random_key = random.choice(chains.keys())

    key_1 = random_key[0]
    key_2 = random_key[1]
    random_w.append(key_1)
    random_w.append(key_2)
    random_v = random.choice(chains[random_key])
    random_w.append(random_v)
    
    while len(random_w) < 20:
        key_1 = random_w[-2]
        key_2 = random_w[-1]
        new_key = (key_1, key_2)
        random_v = random.choice(chains[new_key])
        random_w.append(random_v)

    new_text = ' '.join(random_w)

    return new_text

def main():
    args = sys.argv


    #allows user to pass a text file to the program in the command line

    # Change this to read input_text from a file
    input_text =  args[1]

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
