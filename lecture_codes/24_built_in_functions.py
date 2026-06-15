def min_abs_indices(s):
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if min_abs == abs(s[i])]

    # or
    # f = lambda i: abs(s[i]) == min_abs
    # filter(f, rangen(len(s))



def largest_adj_sum(s):
    return max([s[i] + s[i+1] for i in range(len(s) - 1)])


    # or
    # return max([a + b for a, b in zip(s[:-1], s[1:])])


def digit_dict(s):
    return {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}

    # or
    # last_digits = [x = x % 10 for x in s]
    # return {d: [x for x in s if x % 10 == d] for d in range(10) if d in last_digits}
    
    
    
def all_have_an_equal(s):
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])

    # or 
    # return min([sum([1 for y in s if y == x] > 1 for x in s)])
    
    # or
    # return min([s.count(x) for x in s]) > 1