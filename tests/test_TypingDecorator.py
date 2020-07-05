import unittest

from Tasks.TypingDecorator import MyClass

class Test_like(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_passing(self):

        self.assertEqual(MyClass().add(5, 5), 10)
        self.assertEqual(MyClass().add(2.5, 22), 24.5)
        self.assertEqual(MyClass().add('f', 7), 'f7')
        self.assertEqual(MyClass().acc(5, 5, 6), 16)
        self.assertEqual(MyClass().acc(5.5, 5, 10.6), 21.1)
        self.assertEqual(MyClass().acc(5.5, 'word', 10.6), '5.5word10.6')

    def test_notpass(self):

        self.assertNotEqual(MyClass().add(5, 5), 55)
        self.assertNotEqual(MyClass().add(2.5, 22), 25.22)
        self.assertNotEqual(MyClass().add('f', 7), 'fffffff')
        self.assertNotEqual(MyClass().acc(5, 5, 6), 556)
        self.assertNotEqual(MyClass().acc(5.5, 5, 10.6), 555106)
        self.assertNotEqual(MyClass().acc(5.5, 'word', 10.6), '55word106')