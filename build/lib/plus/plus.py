cache = {}


def isPresent(first, second):
    """
    Check if a pair is present in the cache
    """
    global cache

    return first in cache and second in cache[first]


def add(first, second, result):
    """
    Add a pair into the cache
    """
    global cache

    cache[first] = {second: result}


def get(first, second):
    """
    Return a pair from the cache, assuming it exists
    """
    global cache

    return cache[first][second]


def plus(first, second):
    """
    Add two numbers together
    """
    # If this pair already exists, get it from the cache
    if isPresent(first, second):
        return get(first, second)

    # Three base cases
    if first == 1 and second == 0:
        return 1

    if first == 0 and second == 1:
        return 1

    if first == 0 and second == 0:
        return 0

    # First number is 0, second isn't:
    # decrement the second number until it also reaches 0 & add 1
    if first == 0:
        val = plus(1, plus(first, second - 1))

        # Add the result to the cache in case it isn't in there yet
        if not isPresent(first, second):
            add(first, second, val)

        return val

    # First number is not 0, second is
    # Base-Base case to add 1 to something without using
    # the '+'-operator
    a = plus(first - 1, second)
    b = 1

    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1

    return a
