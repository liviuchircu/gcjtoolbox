# gcjtoolbox
Google Code Jam productivity tools for Python

## 0. Quick Install

    git clone https://github.com/liviuchircu/gcjtoolbox ~/src/gcjtoolbox
    echo 'export PYTHONPATH=$PYTHONPATH:~/src/gcjtoolbox' >> ~/.bashrc
    source ~/.bashrc
    python3 -c 'import gcjtoolbox'

## 1. Focus on the solution

```python
""" https://github.com/liviuchircu/gcjtoolbox """
from gcjtoolbox import GCJ

# for each test case, read the whole input (one line here), output a 0
def solve_case(f):
    line = f.readline()[:-1]
    return 0

# run all the tests, write results to <infile>.out
GCJ(solve_case)
```

## 2. Just run it. Even with no arguments.

```
]$ python3 A.py
Finding latest modified input file...
Moved file: /home/liviu/Downloads/A-large-practice.in to ./A-large-practice.in

Processing ./A-large-practice.in...
Ran 100 tests in 0.11s (min=0.00s, avg=0.00s, max=0.02s)
Wrote 100 answers to ./A-large-practice.out
```

## More options

    python3 A.py --help
