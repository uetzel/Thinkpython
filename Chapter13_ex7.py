"""
Author: Usman Kotwal
Date: 22 May 2020
Exercise taken from: http://greenteapress.com/thinkpython2/html/thinkpython2014.html
"""
"""
To choose a random word from the histogram, the simplest algorithm is to build a list with 
multiple copies of each word, according to the observed frequency, and then choose from the list:

def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)

    return random.choice(t)
The expression [word] * freq creates a list with freq copies of the string word. The extend 
method is similar to append except that the argument is a sequence.

This algorithm works, but it is not very efficient; each time you choose a random word, it rebuilds 
the list, which is as big as the original book. An obvious improvement is to build the list once and 
then make multiple selections, but the list is still big.

An alternative is:

1 Use keys to get a list of the words in the book.
2 Build a list that contains the cumulative sum of the word frequencies (see Exercise 2). 
The last item in this list is the total number of words in the book, n.
3 Choose a random number from 1 to n. Use a bisection search (See Exercise 10) to find the 
index where the random number would be inserted in the cumulative sum.
4 Use the index to find the corresponding word in the word list.

Exercise 7  
Write a program that uses this algorithm to choose a random word from the book. 
Solution: http://thinkpython2.com/code/analyze_book3.py.
"""
from random import randint
from bisect import bisect

from Chapter13 import word_to_dict


def text_into_list(hist):
    # returns a list of the words in the book
    t = []
    for keys in hist:
        t.append(keys)
    return(t)


def word_frequency_list(hist):
    # returns the frequency values of the words used in the book
    t = []
    for key, value in hist.items():
        t.append(value)
    return(t)



def cumulative_frequency(word_frequency_list):
    """
    cumu: list where entries are cumulations of the wordfrequency. It is sorted by the first time the word 
    is used in the text. 
    
    e.g. "Hello my dear darling. Today is a good day. It really is nice to be there and say hello, my dear"
    >> "Hello" has a freq of 2 and is the first word and third to last, so the cumulative list entry at 0 would be [2]
    >> "my" has a freq of 2 and is the second word and the second to last. So the cumulative list would look like
    [2, 4] because >>2 for hello and additional 2 for my<<. 
    """
    cumu = []
    counter = 0
    for i in word_frequency_list:
        counter += i
        cumu.append(counter)
    return(cumu)


def bisect_search(cumulative_frequency):
    """
    random_number = a random number between 0 and the last entry in the cumulative list of word frequencies
    """
    random_number = randint(0, cumulative_frequency[len(cumulative_frequency)-1])
    index_in_cumufreq_list = bisect(cumulative_frequency, random_number)
    return(index_in_cumufreq_list)

def corresponding_word_to_frequency(hist):
    """
    the random number is input into the bisect_search of the cumu_freq and the corresponding index is
    used for the list of words.
    """
    index = bisect_search(cumulative_frequency)
    print(index)
    t = text_into_list(hist)
    print(t[index])


if __name__ == '__main__':
    hist = word_to_dict()
    word_frequency_list = word_frequency_list(hist)
    cumulative_frequency = cumulative_frequency(word_frequency_list)
    corresponding_word_to_frequency(hist)
