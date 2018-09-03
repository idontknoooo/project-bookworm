# Slicing can be extended to any python class by method
__getitem__
__setitem__
# see item 28

# Slicing arr[inclusive:exclusive]
arr[start:end]
# 0 or len(arr) is redundent in slicing, can omit

# Assign to list slice will replace the slice, even if the length is not same
a = [1,2,3]
a[:2] = [1,2,3,4,5]
# a -> [1,2,3,4,5,3]
