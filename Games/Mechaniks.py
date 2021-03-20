import random
class fight():
    def attack(self,P1):
        rnd=fight()
        if int(P1.strength) >int(P1.agility) and int(P1.strength) >int(P1.intelligence):
            P=0
        elif int(P1.agility) >int(P1.strength) and int(P1.agility) >int(P1.intelligence):
            P=1
        else:
            P=3
        
        if P==0:
            print("vblizi")
            return int(rnd.chanse())*(int(P1.strength)//3)
        elif  P==1:
            print("Kreets")
            return (int(rnd.chanse())+1)*(int(P1.strength)//2)
        else:  
            print("magik")
            return int(rnd.chanse())*(int(P1.intelligence)//3)
    def doge(self,P):
        rnd=fight()
        a=rnd.chanse()
        if int(P.agility) < 6:
            if a==0:
                print("ne uklon")
                return 0 
            elif a==1:
                print(" uklon")  
                return 1 
            else:
                print(" ne uklon") 
                return 0 
        elif int(P.agility) >6 :
            if a==0:
                print("uklon") 
                return 1 
            elif a==1:
                print("ne uklon")
                return 0   
            else:
                print(" uklon")
                return 1 
        else:
            print("ubezjal")
            return 0 
                
                   
    def time(self,P1,P2):
        P=1
        a=1
        i=0
        Pol=1
        foolo=fight()
        P1_health=int(P1.heath)
        P2_health=int(P2.heath)
        print("hearth_1=",P1_health)
        print("hearth_2=",P2_health)
        while a==1:
            print("step  ____________________",i)
            if P1_health<=0 or P2_health<=0:
                a=0 
            else:
                if P==1:
                    P-=1
                    
                    yron=foolo.attack(P1)
                    if foolo.doge(P2)==0:
                        P2_health-=yron
                    
                    print("hearth_1=",P1_health)
                    print("hearth_2=",P2_health)
                    Pol=1
                else :
                    yron=foolo.attack(P2)
                    if foolo.doge(P1)==0:
                        P1_health-=yron
                    
                    P+=1
                    print("hearth_1=",P1_health)
                    print("hearth_2=",P2_health) 
                    Pol=2
            i+=1      
        return Pol   
     
    def chanse(self):
        a=random.randint(0,2)
        return  a  

class mechan():       
    def move(self):
        print("sobaka")
        
   
    





