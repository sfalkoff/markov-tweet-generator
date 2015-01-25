#!/usr/bin/env python

import sys
import random
from sys import argv

# import os
# import twitter

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    # Remove trailing characters from corpus and split into a list of words
    text = corpus.rstrip().split()

    # Initialize the dictionary that will hold the Markov chains
    chains_dict = {}
    
    # Iterate over the corpus text, defining key value pairs to make chains
    for i in range(len(text) - 2):

        # The key is a tuple containing two words
        key = (text[i], text[i + 1])
        value = text[i + 2]
        
        # Add to dictionary
        if key in chains_dict:
            chains_dict[key].append(value)
        else:
            chains_dict[key] = [value] #initializes value as a list
        
    return chains_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    # Initialize empty list to store random words to make text
    random_word = []

    # Select a random key (a tuple)
    random_key = random.choice(chains.keys())

    # Save each value in the random key to a variable
    key_1 = random_key[0]
    key_2 = random_key[1]

    # Add each word from the random key to random word list
    random_word.append(key_1)
    random_word.append(key_2)

    # Select a random value from the list of values associated with the random key and add to random word list
    random_value = random.choice(chains[random_key])
    random_word.append(random_value)
    
    while len(random_word) < 30:
        # Create new key from the last two items added to random word list
        key_1 = random_word[-2]
        key_2 = random_word[-1]
        new_key = (key_1, key_2)

        # Get the list of values associate with the new key, select a word value randomly and add to random word list
        random_value = random.choice(chains[new_key])
        random_word.append(random_value)

    # Join random word list into a string
    new_text = ' '.join(random_word)

    return new_text

#def tweet_mash(markov_text):
        # # access secret keys
    # TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
    # TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
    # TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
    # TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

    # api = twitter.Api(
    #     consumer_key=TWITTER_CONSUMER_KEY,
    #     consumer_secret=TWITTER_CONSUMER_SECRET,
    #     access_token_key=TWITTER_ACCESS_TOKEN,
    #     access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
    # )

    # #EDIT THIS LINE:
    # status = api.PostUpdate("Hello")

def main():

    # Allows user to pass Python script and two text files to the program in the command line
    script, filename1, filename2 = argv

    # Open and read both files, then combine them into one input_text string
    file_1 = open(filename1)
    input_text = file_1.read()
    file_2 = open(filename2)
    input_text = input_text + file_2.read()

    # Close both files
    file_1.close()
    file_2.close()

    # Call chain_dict and random_text to create Markov text
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()


