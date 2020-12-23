cache = {}


def plus(first, second):
    """
    Main function that checks certain conditions
    """
    # Check if both arguments are integers
    if not (isinstance(first, int)):
        raise TypeError(f"First argument ({first}) is not an integer.")

    if not (isinstance(second, int)):
        raise TypeError(f"Second argument ({second}) is not an integer.")

    # The function does -1 until both arguments reach 0,
    # so this isn't possible for negative integers
    if first < 0:
        raise ValueError(f"First argument ({first}) is not a negative integer.")

    if second < 0:
        raise ValueError(f"Second argument ({second}) is not a negative integer.")

    return _plusRecursive(first, second)


def _plusRecursive(first, second):
    """
    Recursive plus function so that all checks only have to happen once
    in the main function above
    """
    # If this pair already exists, get it from the cache
    if _isPresent(first, second):
        return _get(first, second)

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
        val = _plusRecursive(1, _plusRecursive(first, second - 1))

        # Add the result to the cache in case it isn't in there yet
        if not _isPresent(first, second):
            _add(first, second, val)

        return val

    # First number is not 0, second is
    # Base-Base case to add 1 to something without using
    # the '+'-operator
    a = _plusRecursive(first - 1, second)
    b = 1

    while b != 0:
        data = a & b
        a = a ^ b
        b = data << 1

    return a


def _isPresent(first, second):
    """
    Check if a pair is present in the cache
    """
    global cache

    return first in cache and second in cache[first]


def _add(first, second, result):
    """
    Add a pair into the cache
    """
    global cache

    cache[first] = {second: result}


def _get(first, second):
    """
    Return a pair from the cache, assuming it exists
    """
    global cache

    return cache[first][second]
