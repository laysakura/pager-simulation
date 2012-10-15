import string
import random

def randstr(n):
    """
    This function returns a random string which has n length.
    The alphabets are [0-9a-zA-Z].
    So randstr(n) can return *42^n* kinds of strings.

    @example
    randstr(10) -> 42^10 = 1.70802e+16
    randstr(12) -> 42^12 = 3.012947e+19
    """
    alphabets = string.digits + string.letters
    return ''.join(random.choice(alphabets) for i in xrange(n))
