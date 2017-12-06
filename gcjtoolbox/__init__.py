"""gcjtoolbox - Google Code Jam tools for speed freaks.

Package currently includes:
    * "GCJ" helper class, which minimizes boilerplate code

Usage Example: below is the simplest possible GCJ solution

    #--------------- A.py -----------------------
    from gcjtoolbox import GCJ

    # for each test case, read the whole input (one line here), output a 0
    def solve_case(f):
        line = f.readline()[:-1]
        return 0

    # run all the tests, write results to <infile>.out
    GCJ(solve_case)
    #-------------------------------------------

Command-line usage:
    python3 A.py # will scan this dir for A*.in and feed it to the program
    python3 A.py A-small-practice.in
    python3 A.py -p /home/foobar/Downloads # additional scan path!

For more info:
    python3 A.py --help
"""

from gcjtoolbox.release import __version__, __author__

from gcjtoolbox.gcj import GCJ, baseToDec, decToBase
from gcjtoolbox.gcj import next_greater_power_of_2, is_power_of_2

__all__ = [ 'GCJ', 'baseToDec', 'decToBase', 'next_greater_power_of_2',
            'is_power_of_2'
            ]
