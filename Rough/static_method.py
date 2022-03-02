
class spam:
    numInstance = 0                    #this variable within the class namespace so behave like static and can be access through class name without instance
    def __init__(self):
        spam.numInstance = spam.numInstance + 1
    def printNumInstance():                     # worked in 3.X but not in 2.x
        print ("Number of instances created : %s" % spam.numInstance)
    def priNumIns(self):                #Here have to pass object as parameter worked in both version 2.X and 3.x
                                        # want to avoid self parameter then have to create static function
        print("Number of instances created : %s" % spam.numInstance)

def printNumInstance():
    print("Number of instance create: %s"% spam.numInstance) #  instead of create in function in class outside will work for all the version
                                                             # Because class variable use as global variable within module namespace
                                                            # disadvantage :- simple function like this cannot customize by inheritance special in large project
if __name__ == '__main__':
    t = spam.printNumInstance   #store function pointer in variable direct from class. It means it is unbound
    obj = spam()               # create object
    t()                        # in 2.X it return error TypeError: unbound method printNumInstance() must be called with spam instance as first argument (got nothing instead)
                               # But working fine in version 3
    spam.printNumInstance()    # same like t()  not working in 2.X but work in version 3
    #t(obj)                     # in both version error "printNumInstance() takes no arguments (1 given)"
    t1 = spam.priNumIns(obj)

    printNumInstance()          # because class
    print("##############below is just code example##########################")
    a , b, c = spam(), spam(), spam()
    #a.printNumInstance()    # return error TypeError: printNumInstance() takes 0 positional arguments but 1 was given
                            # because calling through the instance
    a.priNumIns()
    spam.priNumIns(a)
    spam().priNumIns()       # first create object spam() and then call the function

