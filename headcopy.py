#!/usr/bin/env python3
"""Play quotes in morse

Usage:
    <program> [speed]
"""

# Modules
import argparse
import sys
import os


# Parse user input
# Adding arguments
parser.add_argument("-v", "--verbose", help="verbosity",
        action="store_true")
parser.add_argument("-n", "--num-eyes", help="number of eyes",
        type=int, default=2, choices=[0,1,2,3,4])

parser.add_argument("-e", "--essential", required=True,
        action="store_true")

either = parser.add_mutually_exclusive_group()
either.add_argument("-a", action="store_true")
either.add_argument("-b", action="store_true")

# Parse arguments
args = parser.parse_args()

# Use arguments
if args.verbose:
    print("You talk the talk")
