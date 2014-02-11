# opens a file named on the command line

from sys import argv

# The command exists returns True if a file exists, based on its name in a string as an argument. 
# It returns False if not.
from os.path import exists

# For sorting the dictionary
import operator

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

    indata = indata.replace('-', ' ')
    # Split indata string on all white space. 
    indata_splitted = indata.split()
    # print indata_splitted

    # Create dictionary.
    dictionary = {}

    for word in indata_splitted:
        # remove punctuation
        word = word.strip(".?,!-'\";_:()*[]")
        # remove capitalization 
        word = word.lower()
        if dictionary.get(word) == None:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    # create new dictionary with entries (frequency, [word list])
    dictionary2 = {}

    for word,frequency in dictionary.items():
        if dictionary2.get(frequency) == None:
            dictionary2[frequency] = [word]
        else:
            dictionary2[frequency].append(word)

    # print dictionary2
    # print "sorted", dictionary2.keys()[::-1]
    values = sorted(dictionary2.keys())
    for frequency in values[::-1]:
        dictionary2[frequency].sort()
        for word in dictionary2[frequency]:
            print word, frequency

    # for values,keys in dictionary2.items():
    #     print values,keys
    # print dictionary2.items()

