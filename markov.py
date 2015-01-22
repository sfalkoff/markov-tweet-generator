#!/usr/bin/env python

import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    #text to open and read
    text_file = open(corpus)
    text_file = text_file.read().split()
    # print text_file
    chains_dict = {}
    for i in range(len(text_file) - 3):
        chains_dict[tuple(text_file[i : i + 2])] = text_file[i + 2]
        #chains_dict[tuple(text_file[text_file[i]:text_file[i + 1]])] = text_file[i + 2]
        # print word
        # print text_file[word + 1]
       # print i
        #print text_file[i]
    print chains_dict
    #remove white space at end of lines
    #split the text into a list of words



    #make a dictrionary
    #return chains_dict
    #dictionary will contain tuples with two words as keys and the value will be a list
    #building the data structure 
    # return {}

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    #using the above data structure to generate random text
    return "Here's some random text."

def main():
    args = sys.argv


    #allows user to pass a text file to the program in the command line

    # Change this to read input_text from a file
    input_text =  args[1]

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text
    print make_chains

if __name__ == "__main__":
    main()
