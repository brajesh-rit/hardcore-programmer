class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj
    def __getattr__(self,attName):
        print('Trace:', attName)
        return getattr(self.wrapped, attName)

if __name__== "__main__":
    x = Wrapper([1,2,3,4])    #Wrap a list
    x.append(9)

    x = Wrapper({'a': 1, 'b': 2})
    list(x.keys())