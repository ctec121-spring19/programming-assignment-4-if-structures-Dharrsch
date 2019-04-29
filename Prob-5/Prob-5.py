# Module 3
#   Programming Assignment 4
#     Prob-5.py

# David Harrsch

def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("There was a type error. Exiting program")
        exit
main()