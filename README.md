# gcjtoolbox
Google Code Jam tools for Python productivity freaks

## 1. Focus on the solution

```python
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
$] python3 A.py
Finding latest modified input file...

Processing ./A-large-practice.in...
Ran 100 tests in 0.11s (min=0.00s, avg=0.00s, max=0.02s)
Wrote 100 answers to ./A-large-practice.out
```

## More options

    python3 A.py --help
