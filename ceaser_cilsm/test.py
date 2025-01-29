import unittest
import ciaser_cipher
class TestingGame(unittest.TestCase):
    def test_game(self):
        answer = ciaser_cipher.cipher("apple", 3 , "encode")
        self.assertEqual("dssoh" , answer)
    def test_game_None(self):
        answer = ciaser_cipher.cipher("123", 3, "12")
        self.assertIsInstance(answer,UnboundLocalError)
    def test_game_None2(self):
        answer = ciaser_cipher.cipher("word", "hi", "encode")
        self.assertIsInstance(answer,ValueError)
