'''
Test module
'''
from functions import mult_check

class TestMultchek:
    '''
    test class for the mult_check function
    '''
    def setup(self):
        '''set up'''
    def test_all(self):
        '''test fizz'''
        result=mult_check(5)
        assert result == 'fizz'
    def test_7(self):
        '''test buzz'''
        result=mult_check(7)
        assert result == 'buzz'
    def test_fizzbuzz(self):
        '''test fizzbuzz'''
        result=mult_check(35)
        assert result == 'fizzbuzz'
    def test_miss(self):
        '''test miss'''
        result=mult_check(11)
        assert result == 'miss'
