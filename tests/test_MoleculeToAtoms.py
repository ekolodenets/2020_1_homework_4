import unittest

from Tasks.MoleculeToAtoms import MyClass

class Test_parse(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parsing(self):

        self.assertEqual(MyClass().parse('H2O'), ({'H': 2, 'O': 1}))
        self.assertEqual(MyClass().parse('Mg(OH)2'), ({'Mg': 1, 'O': 2, 'H': 2}))
        self.assertEqual(MyClass().parse('K4[ON(SO3)2]2'), ({'K': 4, 'O': 14, 'N': 2, 'S': 4}))
        self.assertEqual(MyClass().parse('Gold23'), ({'Gold': 23}))
        self.assertEqual(MyClass().parse('Golden3(Eye6)6'), ({'Golden': 3, 'Eye': 36}))
        self.assertEqual(MyClass().parse('K4Fl4{G2[ON(Sn2)2]2H2}2Gy'), ({'K': 4, 'Fl': 4, 'G': 4, 'O': 4, 'N': 4, 'Sn': 16, 'H': 4, 'Gy': 1}))

    def test_notparsing(self):

        self.assertNotEqual(MyClass().parse('H2O'), ({'H': 1, 'O': 1}))
        self.assertNotEqual(MyClass().parse('Mg(OH)2'), ({'Mg': 0, 'O': 2, 'H': 2}))
        self.assertNotEqual(MyClass().parse('K4[ON(SO3)2]2'), ({'K': 4, 'O': 1, 4: 2, 'S': 4}))
        self.assertNotEqual(MyClass().parse('K4Fl4{G2[ON(Sn2)2]2H2}2Gy'), ({'K': 4, 'Fl': 4, 'G': 4, 'O': 4, 'N': 4, 'Sn': 1, '6H': 4, 'Gy': 1}))