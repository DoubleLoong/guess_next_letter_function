import unittest
from guess_next_letter_function import guess_next_letter
class GuessTest(unittest.TestCase):
    """用于测试guess_next_letter_function.py"""
    def test_guess_next_letter1(self):
        """是否能得到正确的下一个字母"""
        guess_letter = guess_next_letter('_____',list())
        self.assertIn(guess_letter,'apple')
    def test_guess_next_letter2(self):
        """是否能得到正确的下一个字母"""
        guess_letter = guess_next_letter('_____',list('b'))
        self.assertIn(guess_letter,'apple')    
    def test_guess_next_letter3(self):
        """是否能得到正确的下一个字母"""
        guess_letter = guess_next_letter('____e',list('ec'))
        self.assertIn(guess_letter,'apple')  
    def test_guess_next_letter4(self):
        """是否能得到正确的下一个字母"""
        guess_letter = guess_next_letter('a___e',list('ecafghjk'))
        self.assertIn(guess_letter,'apple')
    def test_guess_next_letter5(self):
        """是否能得到正确的下一个字母"""
        guess_letter = guess_next_letter('app_e',list('ecafghjkp'))
        self.assertIn(guess_letter,'apple') 
if __name__=='__main__':
    unittest.main()