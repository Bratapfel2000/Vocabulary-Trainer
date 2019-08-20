from random import *
import csv

"""
vokabeltrainer2000, version 0.1
written in python 3.7
"""

vocabulary_file = 'xyz.csv'

#csv file reader
def readMyFile(filename):
    lang1 = []
    lang2 = []
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            lang1.append(row[0])
            lang2.append(row[1])
    return lang1, lang2
lang1,lang2 = readMyFile(vocabulary_file)

#takes a random number from range of length of vocabulary_file
def lang1_lang2_rand_picker():
    lang1,lang2 = readMyFile(vocabulary_file)
    length_dict =len(lang1)
    rand_no = randint(0, length_dict-1)
    return rand_no

#enter amount of words you want to be asked
def how_many_words():
    howmany = int(input("How many words to check?: "))
    print(" ")
    return howmany

#ask amount of words, in random direction
def lang1_lang2_count():
    j = 0
    k = 0
    lang1,lang2 = readMyFile(vocabulary_file)
    howmany = how_many_words()
    for i in range(howmany):
        rand_no = lang1_lang2_rand_picker()
        input_lang = input("What is '"+lang1[rand_no]+"' in German?: ")
        if input_lang == lang2[rand_no]:
            j += 1
            print("Correct:", j)
            print(" ")
        else:
            k += 1
            print("Wrong:", k, "    Correct answer is: ", lang2[rand_no])
            print(" ")
    print(" ")
    print(5*"-","Result", 5*"-")
    print("Correct:",j, "Wrong:", k)

lang1_lang2_count()

