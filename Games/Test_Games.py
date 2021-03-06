import unittest
import Mechaniks
import Personal
import random
import Move

class P1(Personal.Player):
    def fool(self):
        print ("soon")

class olimTest(unittest.TestCase):
    def test_Na_rasstoyanie_daleko(self):
        self.assertEqual(Move.mechan.proverk(self, ["*", "-","-","-","-","%"], 1), 1)
    def test_Na_rasstoyanie_blizko(self):
        self.assertEqual(Move.mechan.proverk(self, [ "-","-","-","-","*","%"], 1), 0) 
    def test_Na_rasstoyanie_MAGA(self):
        self.assertEqual(Move.mechan.proverk(self, [ "-","-","-","*","-","%"], 0), 0)    
    def test_Na_rasstoyanie_MAGA_daleko(self):
        self.assertEqual(Move.mechan.proverk(self, [ "-","-","*","-","-","%"], 0), 1)        
         
    def test_step_vpered_P1(self):
        self.assertEqual(Move.mechan.movevperedP1(self, ["*","-","-","-","-","%"]),["-","*","-","-","-","%"])   
    def test_step_vpered_P2(self):
        self.assertEqual(Move.mechan.movevperedP2(self, ["*","-","-","-","-","%"]),["*","-","-","-","%","-"])  
    def test_step_nazad_P1(self): 
        self.assertEqual(Move.mechan.movenavadP1(self, ["-","*","-","-","%","-"]),["*","-","-","-","%","-"])
    def test_step_nazad_P2(self): 
        self.assertEqual(Move.mechan.movenavadP2(self, ["-","*","-","-","%","-"]),["-","*","-","-","-","%"])  
        
    def test_doge_do_6_1(self):
        classTest=P1()
        classTest.strength=5
        classTest.agility=1
        classTest.intelligence=8
        self.assertEqual(Mechaniks.fight.doge(self,classTest),0)    
   
    
    def test_doge_posle_6(self):
        classTest=P1()
        classTest.strength=5
        classTest.agility=8
        classTest.intelligence=1
        self.assertEqual(Mechaniks.fight.doge(self,classTest),1) 
        
    def chanse_test_0(self):
        self.assertEqual(Mechaniks.fight.chanse(self),0)
    
    def time_1(self):
        classTest1=P1()
         
        classTest1.strength=8
        classTest1.agility=1
        classTest1.intelligence=1
        classTest1.heath=18
        classTest1.mana=4
        classTest1.dodge=4
        
        classTest2=P1()
        classTest2.strength=4
        classTest2.agility=1
        classTest2.intelligence=8
        classTest2.heath=12
        classTest2.mana=10
        classTest2.dodge=6
        
        self.assertEqual(Mechaniks.fight.time(self, classTest1, classTest2),0)                    
if __name__ == '__main__':
    unittest.main()