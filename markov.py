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
    # for k, v in chains_dict.items():
    #     if k in chains_dict:
    #         chains_dict[k] = chains_dict + chains_dict[v]

    for i in range(len(text_file) - 2):
        # if k in chains_dict:
        #     chains_dict[k] = chains_dict + chains_dict[v]
        chains_dict[tuple(text_file[i : i + 2])] = list([text_file[i + 2]])
    print chains_dict




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
