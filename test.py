import operator

states = {
    'Oregon': '67',
    'Florida': '2',
    'California': '99', 
    'New York': '1', 
    'Michigan': '46'
    }


# s = sorted(states.iteritems(), key = operator.itemgetter(1))

# print s
# print s[::-1]

# We could also create a list of keys or values and sort by key/value list, 
# then access the diciontary to print the relevant items in order


s2 = states.values()

print sorted(s2, key=int, reverse=True)

s3 = states.keys()
s3.sort()

print s3

