# coding: utf-8 
import unittest
import password as pwd
  
class TestPassword(unittest.TestCase):
     
    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getLenNormal(self):
        self.assertEqual(len(pwd.getNext("abcd")), 4)
        
    def test_getLenEndLine(self):
        self.assertEqual(len(pwd.getNext("zzzz")), 6) #erreur = 6
    
    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")
        
    def test_hasSeries(self):
        self.assertTrue(pwd.hasSeries("abc"), True)
        
    def test_hasSeries(self):
        self.assertTrue(pwd.hasSeries("aabc"), True)
        
    def test_hasTwoPairs(self):
        self.assertTrue(pwd.hasTwoPairs("aabbc"), True)
        
    def test_hasTwoPairs(self):
        self.assertFalse(pwd.hasTwoPairs("aabc"), True)
        
    def test_hasNoBadChar(self):
        self.assertTrue(pwd.hasNoBadChar("aabc"), True)
        
    def test_hasNoBadChar(self):
        self.assertFalse(pwd.hasNoBadChar("aibc"), True)
        
    def test_hasNoBadChar(self):
        self.assertFalse(pwd.hasNoBadChar("aobc"), True)
        
    def test_hasNoBadChar(self):
        self.assertFalse(pwd.hasNoBadChar("albc"), True)
       
     
     
# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()

