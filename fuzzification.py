import numpy as np
import skfuzzy as fuzz

#class Fuzzification:

 #   def __init__(self):



class Input:

    def __init__(self, name, _type, params ):
        self.name = name
        valuer = np.array([20])
        HumPRange = np.array([-45,0,45])
        HumidP = MembershipFunction("trimf", HumPRange, valuer)


    def trimf(self, _input, params):
        
    

class MembershipFunction:

    def __init__(self, _type, Mrange,valueToFuzz):
        self.type = _type #trap or triangular
        self.range = Mrange
        self.mbf = None
        self.toFuzz = valueToFuzz
        #self.MakeFunction(value, self.range)
        
        print(self.type)
        print(self.range)
        print(self.mbf)
        print(self.toFuzz)
        

        
    def MakeFunction(self, value, Mrange):

        print("Make Funct")
    
        
        mbf = fuzz.trimf(value, Mrange)

        print(mbf)

#class medium:

#class excellent:
i = Input()
