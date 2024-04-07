import unittest

def is_palindrome(value):
    start = 0
    end = len(value) - 1
    
    while start < end:
        if value[start] != value[end]:
            return False
        start += 1
        end -= 1
    
    return True

class TestIsPalindrome(unittest.TestCase):

    def test_with_a(self):

        input = "a"
        result = is_palindrome(input)
        self.assertTrue(result)



    def test_with_ala(self):

        input = "ala"
        result = is_palindrome(input)
        self.assertTrue(result)



    def test_with_neuquen(self):

        input = "neuquen"
        result = is_palindrome(input)
        self.assertTrue(result)



    def test_with_hola(self):

        input = "hola"
        result = is_palindrome(input)
        self.assertFalse(result)





unittest.main()


