#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    if len(a_dictionary.value()) == 0:
        return None

    max_value = max(a_dictionary.value())

    for key, value in a_dictionary.items():
        if value == max_value:
            return key
