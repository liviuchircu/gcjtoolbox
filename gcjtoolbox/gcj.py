"""GCJ problem helper module
"""

import os, sys, shutil
import argparse, time

class GCJ:
    """
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
    def __init__(self, solve_case_f):
        fn = sys.argv[0]
        prefix = fn.split('.')[0]

        parser = argparse.ArgumentParser(description=
                "GCJ Helper Framework. "
                "If no input file is given, the current dir will be searched "
                "for the most recently changed \"{}*.in\" input file. If such "
                "a file is found, it is fed to the program. "
                "For best results, name your solution files [ABCDEF].py"
                .format(prefix))
        group = parser.add_mutually_exclusive_group()
        group.add_argument("file", nargs='?',
                           help="Google Code Jam \"*.in\" file")
        group.add_argument("-p", "--path",
                   help="Additional directory to be included in the scan "
                   "for the most recent \"{}*.in\" input file".format(prefix))
        opts = parser.parse_args()

        """ https://stackoverflow.com/a/4500607/2054305 """
        def sorted_ls(path_list, prefix='A', suffix='.in'):
            mtime = lambda f: -os.stat(f).st_mtime
            matches = []
            for path in path_list:
                if not os.path.exists(path):
                    continue

                matches += [os.path.join(path, f) for f in \
                       os.listdir(path) if f[0] == prefix and f[-3:] == suffix]
            return list(sorted(matches, key=mtime))

        if prefix not in ['A', 'B', 'C', 'D', 'E', 'F']:
            print("WARNING: non-standard solution file name: {}!".format(fn))
            if not opts.file:
                print("No input file!")
                return

        if len(sys.argv) > 2:
            print("WARNING: Ignoring additional input files")

        if not opts.file:
            print("Finding latest modified input file...")
            extra_path = opts.path or '/home/liviu/Downloads'
            allfiles = sorted_ls(['.', extra_path], prefix)
            if not allfiles:
                print("Failed to find a file matching {}*.in!".format(prefix))
                return

            input_file = allfiles[0]
            dirname = os.path.dirname(input_file)

            if dirname != '.':
                new_file = os.path.join('.', os.path.basename(input_file))
                shutil.move(input_file, new_file)
                print("Moved file: {} to {}".format(input_file, new_file))
                input_file = new_file
        else:
            input_file = opts.file

        print("\nProcessing {}...".format(input_file))

        with open(input_file, 'r') as fi:
            output_file = input_file.replace("in", "out")
            with open(output_file, "a") as fo:
                fo.truncate(0)
                T = int(fi.readline())
                if __debug__:
                    times = []
                for case in range(1, T+1):
                    if __debug__:
                        st = time.time()
                    answer = solve_case_f(fi)
                    if answer[-1] == '\n':
                        answer = answer[:-1]
                    fo.write("Case #{}: {}\n".format(case, answer))
                    if __debug__:
                        times.append(time.time() - st)
            if __debug__:
                print("Ran {} tests in {:.2f}s "
                        "(min={:.2f}s, avg={:.2f}s, max={:.2f}s)".format(
                        T, sum(times), min(times), sum(times)/T, max(times)))
            print("Wrote {} answers to {}".format(T, output_file))

def next_greater_power_of_2(x):
    return 2**(x).bit_length()

def is_power_of_2(x):
    return not (x & (x - 1))
