# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

from twttr import shorten


def test_shorten():
    assert shorten('CS50P') == 'CS50P'
    assert shorten('twitter') == 'twttr'


def test_caps():
    assert shorten('Cs50q') == 'Cs50q'
    assert shorten('tWitteR') == 'tWttR'


def test_number():
    assert shorten('23U23') == '2323'
    assert shorten('0o0') == '00'

def test_smth():
    assert ...


"""
How to Test
To test your tests, run pytest test_twttr.py. Be sure you have a copy of a twttr.py file in the same folder. Try to use correct and incorrect versions of twttr.py to determine how well your tests spot errors:

Ensure you have a correct version of twttr.py. Run your tests by executing pytest test_twttr.py. pytest should show that all of your tests have passed.
Modify the correct version of twttr.py in such a way as to create a bug. Your program might, for example, mistakenly only omit lowercase vowels! Run your tests by executing pytest test_twttr.py. pytest should show that at least one of your tests has failed.
"""