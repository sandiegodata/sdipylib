
# Copyright (c) 2016 San Diego Regional Data Library This file is licensed under the terms of the
# Revised BSD License, included in this distribution as LICENSE

"""

"""

import re


def make_acro(past, prefix, s):  # pragma: no cover
    """Create a three letter acronym from the input string s, with a best effort to create
    one that is mnemonic for the input string

    Args:
        past: A set object, for storing acronyms that have already been created
        prefix: A prefix added to the acronym before storing in the set
        s: The string to create the acronym from.
    """

    def _make_acro(s, t=0):
        """Make an acronym of s for trial t. The trial is an int from 0 to 10 with alternatives for
        creating an acronym, so if one rule doesn't create something unique, maybe a later one can. """

        # Really should cache these ...
        v = ['a', 'e', 'i', 'o', 'u', 'y']
        c = [chr(x) for x in range(ord('a'), ord('z') + 1) if chr(x) not in v]

        s = re.sub(r'\W+', '', s.lower())

        vx = [x for x in s if x in v]  # Vowels in input string
        cx = [x for x in s if x in c]  # Consonants in input string

        if s.startswith('Mc'):

            if t < 1:
                return 'Mc' + v[0]
            if t < 2:
                return 'Mc' + c[0]

        if s[0] in v:  # Starts with a vowel
            if t < 1:
                return vx[0] + cx[0] + cx[1]
            if t < 2:
                return vx[0] + vx[1] + cx[0]

        if s[0] in c and s[1] in c:  # Two first consonants
            if t < 1:
                return cx[0] + cx[1] + vx[0]
            if t < 2:
                return cx[0] + cx[1] + cx[2]

        if t < 3:
            return cx[0] + vx[0] + cx[1]
        if t < 4:
            return cx[0] + cx[1] + cx[2]
        if t < 5:
            return cx[0] + vx[0] + vx[1]
        if t < 6:
            return cx[0] + cx[1] + cx[-1]

        # These are punts; just take a substring

        if t < 7:
            return s[0:3]
        if t < 8:
            return s[1:4]
        if t < 9:
            return s[2:5]
        if t < 10:
            return s[3:6]

        return None

    for t in range(11): # Try multiple forms until one isn't in the past acronyms

        try:
            a = _make_acro(s, t)

            if a is not None:
                if prefix:
                    aps = prefix + a
                else:
                    aps = a

                if aps not in past:
                    past.add(aps)
                    return a

        except IndexError:
            pass

    raise Exception("Could not get acronym for {}".format(s))

