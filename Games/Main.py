import Personal
import Mechaniks

class P1(Personal.Player):
    def fool(self):
        print ("soon")
class P2(Personal.Player):
    def fool(self):
        print ("soon")

class fight(Mechaniks.fight):
    def fool(self):
        print ("soon")
    
def main():
    
    FP1=P1()    
    FP2=P2()
    figth=fight()
    print ("First player vvedite harakters")
    FP1.inicialization()  
    print (" player vvedite harakters")      
    FP2.inicialization()
    print("fight")
    winner=figth.time(FP1, FP2)
    print("winner personaj",winner)


def run():
    print("start")
    main()
    
    
    
    
run()