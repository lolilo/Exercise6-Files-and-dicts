

# string.split()
# string.strip()
# dict.get()
# dict.iteritems()


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

    # Split indata string on all white space. 
    indata_splitted = indata.split()
    # print indata_splitted

    

    # Create dictionary.
    dictionary = {}

    for word in indata_splitted:
        # remove punctuation
        word = word.strip(".?,!")
        # remove capitalization 
        word = word.lower()
        if dictionary.get(word, None) == None:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    

    # Sort the output from the highest frequency words to the lowest frequency words.
    dictionary_frequency_sorted = sorted(dictionary.iteritems(), 
        key = operator.itemgetter(1), reverse = True)
    # print dictionary_frequency_sorted
    # Remember, you can't order a dictionary. Must create a list for order. 

    # Determine highest frequency. 
    highest_count = dictionary_frequency_sorted[0][1]
    # Initialize new dictionary.
    alphabetized_dictionary = {}

    # Populate dictionary with keys from 1 to highest_count. Set values to lists.
    for count in range(highest_count):
        alphabetized_dictionary[count + 1] = []

    for i in range(len(dictionary_frequency_sorted)):
        frequency = dictionary_frequency_sorted[i][1]
        alphabetized_dictionary[frequency].append(dictionary_frequency_sorted[i][0])
    # print "alphabetized_dictionary", alphabetized_dictionary
    
    # Alphabetize the values in the alphabetized_dictionary.
    for entry in range(highest_count):
        alphabetized_dictionary[entry + 1].sort()

    # print "\nalphabetized_dictionary after alphabetizing", alphabetized_dictionary

    for entry in range(highest_count)[::-1]:
        for word in alphabetized_dictionary[entry + 1]:
            print word, entry + 1

    # for entry in dictionary_frequency_sorted:
    #     print entry[0], entry[1]


    # Understand the difference between dict.item() and dict.iteritems()        
    # for key,value in dictionary.iteritems():
    #     print key, value

    isValid = False

