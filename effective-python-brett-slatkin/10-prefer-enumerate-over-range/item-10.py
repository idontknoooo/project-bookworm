# Enumerate vs Range
#   Enumerate
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))
#   Range
for i in range(len(flavor_list)):
    print('%d: %s' % (i + 1, flavor_list[i]))

# Enumerate syntax is clearer
# Prefer enumerate over range

# If don't need second parameter
for i, _ in enumerate(flavor_list):
    print i
