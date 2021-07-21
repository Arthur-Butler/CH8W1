from profanity_filter import ProfanityFilter
strVal="hello"



class charClass:
    def __init__(self,inputVar):
        self.inputVar=inputVar
        
    def valFunc(self):
        charArr= ["@","#","$","%","^","&","*","(",")"]
        for i in range(len(self.inputVar)):
            for n in range(len(charArr)):
                if self.inputVar[i]==charArr[n]:
                    return True
                else:
                    return False
                    
class numClass:
    def __init__(self,inputVar):
        self.inputVar=inputVar
        
    def valFunc(self):
        numArr= [1,2,3,4,5,6,7,8,9,0]
        for i in range(len(self.inputVar)):
            for n in range(len(numArr)):
                if self.inputVar[i]==numArr[n]:
                    return True 
                else:
                    return False                
    
class swearClass:
    pf = ProfanityFilter()
    def __init__(self,inputVar):
        self.inputVar=inputVar
        
    def valFunc(self):
        for i in range(len(self.inputVar)):
            for y in range(len(swearArr)):
                    if  pf.is_profane(self.inputVar)==True:
                        return True
                    else:
                        return False
                        
class upperClass:  
    def __init__(self,inputVar):
        self.inputVar=inputVar
        
    def valFunc(self):
        for i in range(len(self.inputVar)):
           if self.inputVar[i].isupper():
               return True
           else:
               return False
 
if 4<len(strVal)<14:              
    if charClass(strVal) == True:
        if numClass(strVal) == True:
            if upperClass(strVal) == True:
                if swearClass(strVal) == False:
                     print("password eligible")
                else:
                    print("password ineligible")
            else:
                print("password ineligible")
        else:
            print("password ineligible")
    else:
        print("password ineligible")
else:
    print("password ineligible")
                    
