

# string.split()
# string.strip()
# dict.get()
# dict.iteritems()


# opens a file named on the command line

from sys import argv

# The command exists returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.
from os.path import exists

# Takes in Python script and one file as arguments. 
script, input_file = argv
isValid = True

# Check if input_file exists.
if not exists(input_file):
    print "%r does not exist!" % input_file
    isValid = False

if isValid:
# Opens and reads input_file.
    in_file = open(input_file)
    indata = in_file.read()

    # Split indata string on all white space. 
    indata_splitted = indata.split()
    # print indata_splitted

    # Create dictionary.
    dictionary = {}

    for word in indata_splitted:
        if dictionary.get(word, None) == None:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    # Understand the difference between dict.item() and dict.iteritems()        
    for key,value in dictionary.iteritems():
        print key, value

    isValid = False

