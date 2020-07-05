import unittest

from Tasks.Like import MyClass

class Test_like(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_passing(self):

        self.assertEqual(MyClass().likes('Mike'), 'Mike likes this')
        self.assertEqual(MyClass().likes('Ulrich'), 'Ulrich hat das gefallen')
        self.assertEqual(MyClass().likes('Paweł, Krzysztof, Yuzef, Zofia, Amelia'), 'Paweł, Krzysztof i 3 innym się spodobało')
        self.assertEqual(MyClass().likes("Max, John, Mark"), 'Max, John and Mark like this')
        self.assertEqual(MyClass().likes("Ulrich Gertrud Ernst "), 'Ulrich, Gertrud und Ernst mögen das')
        self.assertEqual(MyClass().likes('Евгений'), 'Евгений это лайкнул(а)')
        self.assertEqual(MyClass().likes('Евгений Андрей Марина'), 'Евгений, Андрей и Марина лайкнули это')

    def test_notpass(self):

        self.assertNotEqual(MyClass().likes('Mike'), 'Mike это лайкнул(а)')
        self.assertNotEqual(MyClass().likes("Max, John, Mark, Евгений"), 'Max, John und Евгений mögen das')
        self.assertNotEqual(MyClass().likes('Евгений'), 'Евгений likes this')
        self.assertNotEqual(MyClass().likes('Ulrich'), 'Ulrich это лайкнул(а)')