class Methods:
    def imeth(self,x):   #Normal instance method passed self object
        print([self, x])
    @staticmethod
    def smeth(x):       # a function no instance passed here later we define as static method
        print([x])
    @classmethod
    def cmeth(cls , x):    # a function get class not instance later we define as class method
        print ([cls, x])

if __name__ == "__main__":
    #smeth = staticmethod(Methods.smeth)    # define static method this will also called as decorator
    #cmeth = classmethod(Methods.cmeth)

    obj = Methods()
    obj.smeth("my name is static method")   #when it define through decorator then working fine but not builtin fuction see line number 12
    obj.smeth("my name is class method")
