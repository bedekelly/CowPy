"""
Created by Bede Kelly.
An implementation of the unix commandline tool 'cowsay'.

Usage: cow.py <message>
"""

import sys

def print_base_cow():
    """Prints the cow's body after the speech bubble."""
    # Slightly odd python, but much more readable.
    cow_list = [r"        \   ^__^",
                r"         \  (oo)\_______",
                r"            (__)\       )\/\ ",
                r"                ||----w |",
                r"                ||     ||"]
    for line in cow_list:
        print(line)  # Generator comps are ugly..

def print_message(message):
    length = len(message) + 2
    print(" ", "_"*length, sep='')
    print("< ", message, " >", sep='')
    print(" ", "-"*length, sep='')

def print_cow(message):
    print_message(message)
    print_base_cow()

# -- Main Code --
def cow_say(message=None):
    if message is not None:
        print_cow(message)
    elif len(sys.argv) == 2:
        message = sys.argv[1]
        print_cow(message)
    else:
        print(__doc__)

if __name__ == "__main__":
    cow_say()
