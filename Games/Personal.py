class  Player:
    strength: int
    agility:int
    intelligence:int
    
    
    heath:int
    mana:int
    dodge:int
    
    def calculation(self):
        self.size = 1
        self.heath = int(self.strength) *3
        self.mana=int(self.intelligence)*2
        self.dodge=int(self.agility)*2
    
    def inicialization (self):
        kolv=15
        print(" --strength------------- u vas" ,kolv," ockov")
        sta=input()
        kolv=kolv-int(sta)
        print(" ----agility----------- ",kolv," ockov")
        agta=input()
        kolv=kolv-int(agta)
        print(" --intelligence------------- ",kolv," ockov")
        itga=input()
        kolv=kolv-int(itga)
        print(" --------------- ")
        
        self.intelligence=(itga)
        self.agility=(agta)
        self.strength=(sta)
        self.calculation()
        self.showinf0()
        
    def showinf0(self):
        print(self.heath)   
        print(self.mana)  
        print(self.dodge)  
        