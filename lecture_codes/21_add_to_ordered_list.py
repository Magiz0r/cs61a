class Link:
    empty = ()
    
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
        
    def __repr__(self):
        if self.rest:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'
        
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def square(x):
    return x * x

def odd(x):
    return x % 2 == 1


def range_link(start, end):
    """
    >>> range_link(3, 6)
    Link(3, Link(4, Link(5)))
    """
    if start >= end:
        return Link.empty
    else:
        return Link(start, range_link(start + 1, end))
    
def map_link(f, s):
    """
    >>> map_link(square, range_link(3, 6))
    Link(9, Link(16, Link(25)))
    """
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))
    
    
def filter_link(f, s):
    """
    >>> filter_link(odd, range_link(3, 6))
    Link(3, Link(5))
    """
    if s is Link.empty:
        return s
    filtered_rest = filter_link(f, s.rest)
    if f(s.first):
        return Link(s.first, filtered_rest)
    else:
        return filtered_rest
    
    
    
def add(s, v):
	"""
	Add v to s, returning modified s.
	
	>>> s = Link(1, Link(3, Link(5)))
	>>> add(s, 0)
	Link(0, Link(1, Link(3, Link(5))))
	>>> add(s, 3)
	Link(0, Link(1, Link(3, Link(5))))
	>>> add(s, 4)
	Link(0, Link(1, Link(3, Link(4, Link(5)))))
	>>> add(s, 6)
	Link(0, Link(1, Link(3, Link(4, Link(5, Link(6))))))
	
	"""
	assert s is not Link.empty
	if s.first > v:
		s.first, s.rest = v, Link(s.first, s.rest)
	elif s.first < v and s.rest == Link.empty:
		s.rest = Link(v)
	elif s.first < v:
		add(s.rest, v)
	return s
    