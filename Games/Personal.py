class  Player:
    strength: int
    agility:int
    intelligence:int
    
    size: int 
    
    heath:int
    mana:int
    dodge:int
    
    def calculation(self):
        self.size = 1
        self.heath = int(self.strength) *3
        self.mana=int(self.intelligence)*2
        self.dodge=int(self.agility)*2
    
    def inicialization (self):
        print(" --strength------------- ")
        self.strength=(input())
        print(" ----agility----------- ")
        self.agility=(input())
        print(" --intelligence------------- ")
        self.intelligence=(input())
        print(" --------------- ")
        self.calculation()
        self.showinf0()
        
    def showinf0(self):
        print(self.heath)   
        print(self.mana)  
        print(self.dodge)  
        