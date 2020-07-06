import unittest

from Tasks.AdvancedCalc import MyClass

class Test_like(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_passing(self):

        self.assertEqual(MyClass().advanced_calc('5'), 5)
        self.assertEqual(MyClass().advanced_calc('5 +75'), 80)
        self.assertEqual(MyClass().advanced_calc('(5 +75)*10'), 800)
        self.assertEqual(MyClass().advanced_calc('2 / 4'), 0.5)
    #
    # def test_notpass(self):
    #
    #     self.assertNotEqual(MyClass().add(5, 5), 55)
