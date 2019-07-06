# ACMICPC-Training
My solutions for some ACM ICPC (https://icpc.baylor.edu) past problems.

# Input Output Management
I wrote a mini input output management library to handle ICPC data.

Below is a simple example on how to test your function to all available samples.
It prints out a line by sample with the success status as well as the time elapsed for the sample.

```py
from input_output_management import run_test

path='past_problems/icpc2019data/B-beautifulbridges/'

def my_function(input):
    """
    My function to solve the problem B-beautifulbridges from icpc2019 WF
    """
    return 'helloworld'

run_test(path, my_function)
```

It also includes timeout handling, hardcoded at 20s at the moment.

Above example would print for example:

> $ python test.py
> status  | sample	| duration
> KO	| sample-1 	| 0.00s
> KO	| sample-2 	| 0.00s
> KO	| secret-01 	| 0.00s
> KO	| secret-02 	| 0.00s
> KO	| secret-03 	| 0.00s
> KO	| secret-04 	| 0.00s
> KO	| secret-05 	| 0.00s
> KO	| secret-06 	| 0.00s
> KO	| secret-07 	| 0.00s

Contributions welcome

# Solutions

https://icpc.baylor.edu/worldfinals/problems
