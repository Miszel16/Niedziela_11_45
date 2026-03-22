import funkcje
import unittest

# - klasa dziedziczy po unittest.TestCase
# - nazwy metod od 'test' (np. test_add)

# 2,4 = 6 Equal
# 3,-3 = 0 Equal

# 3,5 != 0 NotEqual

# class Test_add(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(funkcje.add(2,4), 6)
#         self.assertNotEqual(funkcje.add(3,5), 0)



class Test_if_palinddrom(unittest.TestCase):
    def test_palindrom(self):
        self.assertEqual(funkcje.if_palindrom("kamilslimak"), True)
        self.assertTrue(funkcje.if_palindrom("ala"))

    def test_not_palindrom(self):
        # wiadro
        # kamyk
        self.assertEqual(funkcje.if_palindrom("wiadro"), False)
        self.assertFalse(funkcje.if_palindrom("kamyk"))



if __name__ == '__main__':
    # runner testów - wyszukije metody 'test...'
    unittest.main()