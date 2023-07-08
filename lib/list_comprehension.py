#!/usr/bin/env python3

def return_evens(num_list):
    even = [x for x in num_list if x%2 == 0]
    print(even)
    return even

def make_exclamation(sentence_list):
    sentences = [sentence + "!" for sentence in sentence_list]
    print(sentences)
    return sentences