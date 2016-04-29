"""
Boilerplate functions for the Google Code Jam.
"""

import sys
import re

infile = None
outfile = None


def initialize():
    """ Opens handles to the input file and output file. """
    global infile, outfile
    if len(sys.argv) < 2:
        print("Input file not specified.")
        sys.exit()
    try:
        infile = open(sys.argv[1], 'r')
        print("Opened input file {}".format(sys.argv[1]))
    except:
        print("Could not open {}".format(sys.argv[1]))
        raise

    # If no output file is provided, construct it from the input filename.
    # If the input filename ends with the suffix ".in", replace the suffix with ".out".from
    # Otherwise, append .out to the input filename.
    if len(sys.argv) < 3:
        # Contruct output file name from input file
        if sys.argv[1].endswith('.in'):
            output_file = re.sub('.in$', '.out', sys.argv[1])
        else:
            output_file = infile + '.out'
    else:
        output_file = sys.argv[2]

    try:
        outfile = open(output_file, 'w')
        print("Opened output file {}".format(output_file))
    except:
        print("Could not open output file {}".format(output_file))
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
    line = "Case #{}: {}".format(case_num, content)
    if verbose:
        print(line)
    print(line, file=outfile)


def end():
    """ Closes open file handles. """
    infile.close()
    outfile.close()
