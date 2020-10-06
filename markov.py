"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()

    return contents


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    words = text_string.split()

    for i in range(len(words) - n):
        link = tuple([words[i+n_index] for n_index in range(n)])
        if chains.get(link) == None:
            chains[link] = [words[i+n]]
        else:
            chains[link].append(words[i+n])
            
    return chains


def make_text(chains, n):
    """Return text from chains."""

    words = []

    # your code goes here
    link = ('a', 'a')
    while(not link[0][0].isupper()):
        link = choice(list(chains.keys()))
    words.extend([word for word in link])

    i = 0
    while chains.get(tuple([words[i+n_index] for n_index in range(n)])):
        words.append(choice(chains[tuple([words[i+n_index] for n_index in range(n)])]))
        i += 1

    return ' '.join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)
print(chains)

# Produce random text
random_text = make_text(chains, 4)

print(random_text)
