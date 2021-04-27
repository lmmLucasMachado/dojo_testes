import unittest
from app import soma, sub, div


class Somateste(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(soma(30,5),35)
        self.assertEqual(soma(40,5),45)
        self.assertEqual(soma(30,2),32)
        self.assertNotEqual(soma(30,5),546)

    def test_sub(self):
        self.assertEqual(sub(40,5),35)
        self.assertEqual(sub(40,-2),42)
        self.assertEqual(sub(-40,-2),-38)
        self.assertNotEqual(sub(40,5),546)
        
    def test_div(self):
        self.assertEqual(div(10,5),2)
        self.assertEqual(div(40,-2),-20)
        self.assertEqual(div(-40,-2),20)
        self.assertEqual(div(-40,0),'nao valida')
        self.assertNotEqual(div(40,5),546)


if __name__=='__main__':
    unittest.main()