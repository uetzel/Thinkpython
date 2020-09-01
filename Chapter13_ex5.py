"""
Author: Usman Kotwal
Date: 21 May 2020
Exercise taken from: http://greenteapress.com/thinkpython2/html/thinkpython2014.html
"""
"""
Exercise 5  
Write a function named choose_from_hist that takes a histogram as defined in Section 11.2 and returns a random
value from the histogram, chosen with probability in proportion to frequency. For example, for this histogram:

>>> t = ['a', 'a', 'b']
>>> hist = histogram(t)
>>> hist
{'a': 2, 'b': 1}
your function should return 'a' with probability 2/3 and 'b' with probability 1/3.
"""
""" 
Next Steps

[x] Write a function that creates a list where each key-entry occurs as many times as the frequency in the 
dict[key] says (the dictionary is as follows {word : frequency_of_word}
"""
from Chapter13 import word_to_dict
import random

def freq_proportional_list():
    """
    list_prop_freq: a list that has the words as many times in it as the frequency of the word in the dict.
    Example: {word: word_frequency} --> {'the': 3}
    The listentry for 'the' should be  list_prop_freq --> [the, the, the]
    """
    list_prop_freq = []
    dict_word_frequency  = word_to_dict()
    for word, freq in dict_word_frequency.items():
        list_prop_freq.extend([word] * freq)
    return(list_prop_freq)


def choose_from_hist():
    t = freq_proportional_list()
    return(random.choice(t))


if __name__ == '__main__':
    for i in range(1000):
        print(choose_from_hist())

