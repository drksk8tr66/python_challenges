#!/usr/bin/env python2
# -*- coding: utf-8 -*-


# Write a function that:
# * Adds default values for keys in person_defaults but not in person
# * Removes keys from person that are not present in person_defaults
def canonicalize_person(person):
    person_defaults = {
        'first_name': 'john',
        'last_name': 'doe',
        'address': 'unknown',
    }

    # Add implementation here
    result = {**person_defaults, **person}
    for x in result.items():
        if x not in person_defaults.keys():
            result.pop(x)
    return result


# This should print:
# {'first_name': 'jane', 'last_name': 'doe', 'address': '864 Old Boerne Rd, Bulverde, Tx'}
print(canonicalize_person({
    'first_name': 'jane',
    'address': '864 Old Boerne Rd, Bulverde, Tx',
    'gender': 'female',
}))
