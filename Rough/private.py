class c1:
    def meth1(self):
        self.__x = 88
        self._b  =  'b'
    def meth2(self):
        print(self.__x)

class c2:
    def metha(self): self.__x = 99
    def methb(self): print(self.__x)

class c3(c1, c2): pass


if __name__ == '__main__':
    I = c3()
    I.meth1()
    I.metha()
    print(I.__dict__)
    I.meth2()
    I.methb()