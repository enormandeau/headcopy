#!/usr/bin/env python3
"""Parse Quote and quotes files modified from pyquotes:
    https://github.com/ik5/pyquotes
"""

# Modules
import random
import sys

# Functions
def iter_quotes(quotes_file):
    "Walks the quotes file, yields a (quote, author) tuple for each quote"

    with open(quotes_file) as f:
        quotes = []

        for line in f:
            if line != SEPARATOR:
                quotes.append(line)
            else:
                if quotes[-1].startswith(AUTHOR_MARK):
                    author = quotes.pop().strip()
                else:
                    author = "Anon"

                yield (''.join(quotes).rstrip(), author)
                quotes = []

# Parse user input
try:
    min_len = int(sys.argv[1])
    max_len = int(sys.argv[2])
except:
    print(__doc__)
    sys.exit(1)

# Global variables
QUOTES_FILE = 'quotes.txt'
SEPARATOR = '----\n'
AUTHOR_MARK = '    '

# Print out one quote
# Limit to quotes of lengths between 40 and 100
quote = ""
author = ""

while len(quote + author) > max_len or len(quote + author) < min_len:
    quote, author = random.choice(list(iter_quotes(QUOTES_FILE)))

print(quote)
print("DE", author)
