
"""
Author: Usman Kotwal
Date: 14 May 2020
Exercise taken from: http://greenteapress.com/thinkpython2/html/thinkpython2014.html
"""

""" 
Exercise 1  
Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, 
and converts them to lowercase.

Hint: The string module provides a string named whitespace, which contains space, tab, newline, etc., and punctuation 
which contains the punctuation characters. Let?s see if we can make Python swear:

>>> import string
>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
Also, you might consider using the string methods strip, replace and translate.

------------------------------------------------------------------------------------------- 

Exercise 2  
Go to Project Gutenberg (http://gutenberg.org) and download your favorite out-of-copyright book in plain text format.

Modify your program from the previous exercise to read the book you downloaded, skip over the header information at 
he beginning of the file, and process the rest of the words as before.

Then modify the program to count the total number of words in the book, and the number of times each word is used.

Print the number of different words used in the book. Compare different books by different authors, written 
in different eras. Which author uses the most extensive vocabulary?

"""


import string



def word_to_dict():
    """
    d: dictionary with all the words from the text file {word:wordcount}
    
    Aim: Read a text file line by line and then read each word. 
    These words should then be stripped of all punctuation and whitespace and added
    to the dictionary _d_ with a counter to measure the frequency of words in 
    the text file 
    """
    d = dict()
    for line in open("greatgatsby.txt"):
        line = line.replace('-', ' ')
        for word in line.split():
            word = word.strip(string.whitespace + string.punctuation)
            word = word.lower()
            d[word] = d.get(word, 0) + 1
    return(d)

def unique_word_counter():
    d = word_to_dict()
    count_unique_words = len(d)
    print(f"There are {count_unique_words} unique words in the text file")
    return(count_unique_words)

def word_counter():
    d = word_to_dict()
    word_count = sum(d.values())
    print(f"There are {word_count} words in total in the text file")
    return(word_count)


def most_used_words():
    """ 
    >>input
    d: dictionary with all the words from the text file {word:wordcount} // from word_to_dict()

    
    Aim: Print how many unique words there are in the text (as every word that is repeated more than once
    will just increase the counter in the _d_). The amount of keys in _d_ equals the amount of unique words.
    Print the top 20 words with highest frequency
    """
    d = word_to_dict()
    most_common = []
    for key, value in d.items():
        most_common.append((value, key))
    most_common.sort(reverse = True)
    for word, freq in most_common[:20]:
        print(word, freq, sep='\t')

def word_dict():
    """
    >>created
    alphaword: Dictionary with all the words from the wordlist (alphabetical list of a loooot of words)

    Aim: Create a dict() with words. This allows for fast lookups!
    """
    alphaword = dict()
    for i in open("words.txt"):
        i = i.strip().lower()
        alphaword[i] = None
    return(alphaword)

def words_from_book_not_in_word_dict():
    """
    Aim: Compare the words from the file with the words from the wordlist. Print all
    the words that are not in the wordlist and count them.
    """
    d = word_to_dict()
    alphaword = word_dict()
    words_not_in_list = dict()
    for key in d:
        if key not in alphaword:
            words_not_in_list[key] = 1
    sum_words_not_in_list = sum(words_not_in_list.values())
    print(f"Here are the words that are not found in the long wordlist provided by Allen: \n{words_not_in_list}.\n"
    f"There are {sum_words_not_in_list} unique words in the textfile.")
