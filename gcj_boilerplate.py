"""
Boilerplate functions for the Google Code Jam.
"""

import sys


infile = None
outfile = None


def initialize():
    """ Opens handles to the input file and output file. """
    global infile, outfile
    if len(sys.argv) < 3:
        print("Input file and output file not specified.")
        sys.exit()
    try:
        infile = open(sys.argv[1], 'r')
    except:
        print("Could not open {}".format(sys.argv[1]))
        raise

    try:
        outfile = open(sys.argv[2], 'w')
    except:
        print("Could not open output file {}".format(sys.argv[2]))
        raise


def read_int():
    """ Reads an integer from the input file. """
    return int(infile.readline().rstrip())


def read_int_list():
    """ Returns a list of integers read from a row in the input file. """
    return [int(i) for i in infile.readline().rstrip().split(' ')]


def read_line():
    """ Returns a line read from the input file. """
    return infile.readline().rstrip()


def output(case_num, content, verbose=True):
    """ Writes a test case to the output file. """
    line = "Case {}: {}".format(case_num, content)
    if verbose:
        print(line)
    print(line, file=outfile)


def end():
    """ Closes open file handles. """
    infile.close()
    outfile.close()
