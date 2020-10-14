class P:
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias

    @property # Getter
    def name(self):
        return self.__name

    """
    @name.setter # Setter... Duh
    def name(self, x):
        self.__name = x
    """  
    
    @name.setter # Fordel ved denne måde
    def name(self, x):
        if x[0] == 'C':
            self.__name = x
        else:
            self.__name = 'CCCCCCC!!!!!!'
        
    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self, x):
        self.__alias = x

# Baaaad Java Style
def get_alias(self):
    return self.__alias

def set_alias(self, x):
    self.__alias = x

    
def get_name(self):
    return self.name

def set_name(self, x):
    self.__name = x