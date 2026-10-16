"""
Функтори - це об'єкти які поводять себе як функція. 
Щоб створити такий об'єкт необхідно описати поведінеку 
магічного метода __call__

"""

class Sample:
    __counter:int
    
    def __init__(self, start:int=0):
        self.__counter = start
    
    @property
    def counter(self):
        return self.__counter
    
    def restart(self):
        self.__counter=0
    
    def __call__(self, *args, **kwds):
        self.__counter+=1
        print("Count of:", self.counter)
        return self.counter

s = Sample(32)
s()
s()
s()
s()
s()
print(s.counter)
s.restart()
s()