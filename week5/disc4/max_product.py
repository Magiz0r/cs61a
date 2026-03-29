def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    # Don't use list operations such as append
    
    # idea: 1. always ignore the 2nd number, and recursion
    #       2. always ignore the 1st number, and recursion
    
    
    length = len(s)
    if length == 1:
        return s[0]
    elif length == 0:
        return 1
            
    return max(max_product(s[1: ]), s[0] * max_product(s[2: ]))