'''
Created on 27/04/2012

@author: jmrua
'''
class First:
    def __init__(self):
        self.__innerVariable = "Soy variable Internal"
    
    def getVariable(self):
        return self.__innerVariable
    
    def setVariable(self, var):
        self.__innerVariable = str(var)
        