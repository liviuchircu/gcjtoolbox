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

## 2. Just run it. No arguments.

```python
python3 A.py

```

## Need help?

    python3 A.py --help
