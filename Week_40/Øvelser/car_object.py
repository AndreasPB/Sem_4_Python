class Car:
    def __init__(self, name, model, bhp, mhp):
        self.name = name
        self.model = model
        self.bhp = bhp
        self.mhp = mhp

    @property
    def name(self):
        return self.__name

    @property
    def model(self):
        return self.__model

    @property
    def bhp(self):
        return self.__bhp

    @property
    def mhp(self):
        return self.__mhp

    @name.setter
    def name(self, x):
        self.__name = x

    @model.setter
    def model(self, x):
        self.__model = x

    @bhp.setter
    def bhp(self, x):
        self.__bhp = x

    @mhp.setter
    def mhp(self, x):
        self.__mhp = x


c = Car

c.mhp = 100
c.name = 'Ulrik'

c.__dict__
print(c.mhp)
c.mhp