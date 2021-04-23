import random
class mechan():
    
    def proverk(self,elements,cl):
        x=1
        if ((elements.index("*")-elements.index("%"))>=-1) or((elements.index("%")-elements.index("*"))<=1):
            x=0
            print("mozno udarit")
            return x
        elif (cl==0 and((elements.index("*")-elements.index("%"))>=-2) or((elements.index("%")-elements.index("*"))<=2)):
                x=0
                print("mozno udarit")
                return x
        else: 
                x=1
                print("mozno nelza")
                print(x)
                return x
    def maps(self,P,elements):
        mesl=mechan()
        kuda=random.randint(0,1)
        
        if P=="*":
            if kuda==0:
                elements=mesl.movevperedP1(elements)
            else:
                elements=mesl.movenavadP1(elements)   
        else:
            if kuda==0: 
                elements=mesl.movevperedP2(elements)
            else:
                elements=mesl.movenavadP2(elements)

        return elements


    def movevperedP1(self,elements):
        elements1=elements
        try: 
            second = "-"
            first = "*"
            fo=elements.index(first)
            elements[fo]=second
            elements[fo+1]=first
            print("move vpered")
            return(elements)
        except ArithmeticError:
            return(elements1)
    def movenavadP1(self,elements):
        elements1=elements
        try:
            second = "-"
            first = "*"
            fo=elements.index(first)
            elements[fo]=second
            elements[fo]=first
            print("move nazad")
            return(elements)
        except ArithmeticError:
            return(elements1)

    def movevperedP2(self,elements): 
        elements1=elements
        try:  
            second = "-"
            first = "%"
            fo=elements.index(first)
            elements[fo]=second
            elements[fo-1]=first 
            print("move vpered")    
            return(elements)   
        except ArithmeticError:
            return(elements1)
    def movenavadP2(self,elements):
        elements1=elements
        try: 
            second = "-"
            first = "*"
            fo=elements.index(first)
            elements[fo+1]=second
            elements[fo]=first
            print("move nazad")
            return(elements) 
        except ArithmeticError:
                return(elements1)  
        
