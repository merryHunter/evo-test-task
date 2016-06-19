#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import shuffle, choice


class EpithetManager:
    """" Class for managing epithets."""

    """ Dictionary for names(keys) and epithets. """
    dict_epithets = {}

    """ Current number of used epithets. """
    counter = 0

    """ Total number of epithets in dictionary. """
    len_epithets = 0

    @classmethod
    def set_epithets_dict(cls, filename):
        """
        Initialize dictionary of epithets. At the beginning, keys are random numbers,
        which will be replaced by usernames on requests.
        :param filename: filename containing a list of epithets in one column
        :return: void
        """
        if not cls.dict_epithets:
            cls.len_epithets = sum(1 for l in open(filename))
            keys = [i for i in range(cls.len_epithets)]
            shuffle(keys)           # randomly shuffle keys if epithets ordered by alphabet
            k = 0
            try:
                with open(filename) as f:
                    for line in f:
                        cls.dict_epithets[keys[k]] = line
                        k += 1
            except IOError as e:
                raise ValueError("Invalid filename!")

    @classmethod
    def get_epithet_dict(cls):
        return cls.dict_epithets

    @staticmethod
    def get_epithet(name):
        """

        :param name: username
        :return: epithet for username picked from <dict_epithets>
        """
        epithet = ""
        man = True
        # Check the gender of username. #
        if name[-1] == u'а':
            man = False

        # For the same user return his epithet. #
        if name in EpithetManager.dict_epithets:
            epithet = EpithetManager.dict_epithets[name]

        elif EpithetManager.counter < EpithetManager.len_epithets:
            epithet = EpithetManager.dict_epithets[EpithetManager.counter]
            if not man:
                epithet = EpithetManager.get_woman_epithet(epithet)
            EpithetManager.dict_epithets[name] = epithet
            del EpithetManager.dict_epithets[EpithetManager.counter]
            EpithetManager.counter += 1

        else:   # If we do not have enough epithets. #
            epithet = choice(EpithetManager.dict_epithets.values())
            e = epithet
            c = e[-1]
            ya = 'я'    # madness, but unicode ruthless
            if not man:
                if repr(c) != repr(ya[-1]):
                    epithet = EpithetManager.get_woman_epithet(epithet)
            else:
                if repr(c) == repr(ya[-1]):
                    epithet = EpithetManager.get_man_epithet_from_woman(epithet)
                    print epithet
            EpithetManager.dict_epithets[name] = epithet

        return epithet

    @staticmethod
    def get_woman_epithet(word):
        word = word.decode('utf-8')
        if word[-1] == '\n':
            word = word[:-1]
        word = word[:-2]
        word = ''.join([c for c in word, u'ая'])
        word = word.encode('utf-8')
        return word

    @staticmethod
    def get_man_epithet_from_woman(word):
        word = word.decode('utf-8')
        word = word[:-2]
        word = ''.join([c for c in word, u'ый'])
        word = word.encode('utf-8')
        return word
