import unittest
import Mechaniks
import Personal

import Move

class olimTest(unittest.TestCase):
    def test_Na_rasstoyanie_daleko(self):
        self.assertEqual(Move.mechan.proverk(self, ["*", "-","-","-","-","%"], 1), 1)
    def test_Na_rasstoyanie_blizko(self):
        self.assertEqual(Move.mechan.proverk(self, [ "-","-","-","-","*","%"], 1), 0) 
         
    def test_step_vpered_P1(self):
        self.assertEqual(Move.mechan.movevperedP1(self, ["*","-","-","-","-","%"]),["-","*","-","-","-","%"])   
    def test_step_vpered_P2(self):
        self.assertEqual(Move.mechan.movevperedP2(self, ["*","-","-","-","-","%"]),["*","-","-","-","%","-"])  
    def test_step_nazad_P1(self): 
        self.assertEqual(Move.mechan.movenavadP1(self, ["-","*","-","-","%","-"]),["-","*","-","-","%","-"])
    def test_step_nazad_P2(self): 
        self.assertEqual(Move.mechan.movenavadP2(self, ["-","*","-","-","%","-"]),["-","*","-","-","%","-"])  
        
   
if __name__ == '__main__':
    unittest.main()