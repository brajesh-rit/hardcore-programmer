class c:
    __slots__ = ['a','b'] # It means only two a and b to attribute is allows so that python reserve only two variable placeholder

class D:
    __slots__ = ['a','b','__dict__']
    c = 3     # here we can able to put new variable due to adding __dict__ in slot it is possible.
              # But this violate the purpose of slots
    def __init__(self):
        self.d = 4        # also working

if __name__ == '__main__':
    x = c()
    x.a = 1  # This is work because a is in the list of slot
    x.__dict__ # give error 'c' object has no attribute '__dict__' . Since it is predefine all two attribute it reserve only just two placeholder

    getattr(x,'a')         # single quote is important.
    setattr(x, 'b',4)      # both getattr and setattr works as usual

    y = D()       # create object y of class D
    y.d           # it is return 4 still it has not contain d .  Because of add __dict__ add in slots.
                  # Adding __dict__ in slot list is dissolve the purpose of slots list

    for attr in list(y.__dict__) + y.__slots__:   #This is working as usual and print all the variable in give object      # two list we can add with + sign
        print(attr, ' => ', getattr(y, attr))          # focus on getattr comma in the parameter

    for attr in list(getattr(y, '__dict__', [])) + getattr(y,'__slots__', []):  # This code exactly same as above
        print(attr, ' => ', getattr(y, attr))