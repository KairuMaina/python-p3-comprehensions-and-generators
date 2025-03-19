#!/usr/bin/env python3
def return_evens(numbers):
    """Returns a list of even numbers from the input list using list comprehension."""
    return [num for num in numbers if num % 2 == 0]

def make_exclamation(sentences):
    """Adds an exclamation mark at the end of each sentence in the list using list comprehension."""
    return [sentence + "!" for sentence in sentences]
