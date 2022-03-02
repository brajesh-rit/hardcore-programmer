
class spam:
    def dot(self,msg):
        print(msg)     # self.x = msg  is not required we can direct parameter call
class selfless:
    def __init__(self, dat):
        self.data = dat
    def selfless(arg1, arg2):              #simple function
        return arg1 + arg2
    def normal(self,arg1, arg2):           #instance expected
        return self.data + arg1 + arg2

def square(arg): return arg ** 2         #simple function (def or lamda)

class sum:
    def __init__(self, val):           #callable instance (ye wala object intialize karne ke liya hai)
        self.value = val
    def __call__(self,arg):            #(ye wala call karne ke liya hai)
        return self.value + arg
class product:
    def __init__(self, val):
        self.value = val
    def __call__(self,arg):
        return self.value * arg        # ye callable method nahi line number 58 me error ata hai agar poject list me rakhte hai to #TypeError: 'product' object is not callable
                                         # because you store instance in that varialbe line# 60  and that instance you are calling with one argument
                                        # But if you pass direct object here then try to print object reference or if you override __repr__ then call that
    def method(self,arg):
        return self.value * arg
    def __repr__(self):
        return str(self.value) + ' repr wala call ho raha hai'

class Negate:
    def __init__(self,val):
        self.val = - val
    def __repr__(self):
        return str(self.val)

if __name__=='__main__':
    obj = spam()
    obj.dot('Hello world')  # normal operation
    obj1 = spam()
    x = obj1.dot            # store the function pointer in variable and then call that variable as function is called "bound method"
    x('Hello brajesh')

    y = spam.dot            # store the function pointer through the class in variable. Then call the function pointer pass first parameter as
    y(obj, "Hello divya")    # object of same class and value of that parameter this type of fuction called "unbound method"

    x = selfless(2)         #it set the value of instance of class attribute "data"
    x.normal(3,4)           # This will return value 2 + 3 + 4 = 6 here 2 comes from instance value data and 3, 4 both comes from parameter
                            # observe function call is through the object instance, so instance attribute pass implicitly
    selfless.normal(x,3,4)    # same output but as above this call through the class and pass the instance explicitly as parameter

    selfless.selfless(2,3)   # ok to call directly from class not required instance to call this because here nothing is used from instance

    #x.selfless(3,4)         # Simple function cannot be call through instance getting below error
                            #TypeError: selfless() takes 2 positional arguments but 3 were given
    #selfless.normal(3,4 )   # received error because normal expect instance through class we cannot call it. it returns errors.
                            #TypeError: normal() missing 1 required positional argument: 'arg2'

    sobject = sum(2)
    pobject = product(3)
    actions = [square, sobject, pobject, product ,pobject.method, Negate ]   # here every element is callable common to get single parameter

    for act in actions:
        print(act(5))
    print ('#######################')
    print(actions[-1](5))
    print('##comprehension call############')
    print([act(5) for act in actions])
    print('## lambda call############')
    print(list(map(lambda act: act(5),actions)))  # ye wala function pointer ko lambda pointer se map karke output deta hai