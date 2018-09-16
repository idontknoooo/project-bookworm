# Closures
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)

numbers = [8,3,1,2,5,4,7,8]
group   = {2,3,5,7}
sort_priority(numbers, group)
print(numbers)
# return: 2 3 5 7 1 4 6 8

# 1. Python supports closures: functions that refer to variables from the scope in which they were defined. This is why the helper function is able to access the 'group' argument to sort_priority.
# 2. Functions are first-class objects in Python, meaning you can refer to them directly, assign them to variables, pass them as arguments to other functions, compare them in expressions and if statements. This is how sort method can accept a closure function as the key argument.
# 3. Python has specific rules for comparing tuples. It first compares items in index zero, then index one, then index two, and so on. This is why the return value from the helper closure causes the sort order to have two distinct groups.

# When reference a variable in an expression, the Python interpreter will traverse the scope to resolve the reference in this order:
# 1. The current function's scope
# 2. Any enclosing (inside) scopes (like other containing functins)
# 3. The scope of the module that contains the code (also called the global scope)
# 4. The built-in scope (that contains functions like len and str)


def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

numbers = [8,3,1,2,5,4,7,8]
group   = {2,3,5,7}
found = sort_priority2(numbers, group)
# Found: False
# Because 'found' is first referred from 'found = False'

# To fix problem above | Python 3
def sort_priority2(values, group):
    found = False
    def helper(x):
        nonlocal found # only available in python 3
        if x in group:
            found = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found

numbers = [8,3,1,2,5,4,7,8]
group   = {2,3,5,7}
found = sort_priority2(numbers, group)

# Python 2
def sort_priority2(values, group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found[0]
# found[0] will find 'found' from outsite, but 'found' is a list, which is mutable

# Avoid using nonlocal statements for anything beyond simple functions.
