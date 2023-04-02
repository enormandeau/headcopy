#!/usr/bin/env python3
"""Parse Quote and quotes files modified from pyquotes:
    https://github.com/ik5/pyquotes
"""

import random
import sys

QUOTES_FILE = 'quotes.txt'
SEPARATOR = '----\n'
AUTHOR_MARK = '    '

def iter_quotes(quotes_file=QUOTES_FILE):
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

if __name__ == '__main__':
    # Print out one quote
    # Limit to quotes of lengths between 40 and 100
    quote = "x" * 500
    author = "x" * 500

    while len(quote + author) > 80 or len(quote + author) < 40:
        quote, author = random.choice(list(iter_quotes()))

    print(quote)
    print("DE", author)
