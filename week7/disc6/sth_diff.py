def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    # activate the iterator
    last = next(t)
    
    # now can use for loop for the iterator
    for x in t:
        yield x - last
        last = x