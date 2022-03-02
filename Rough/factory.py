def fact_ory(aclass, *arg, **kwargs):
    return aclass(*arg, **kwargs)

class Spam:
    def __init__(self,msg):
        self.msg = msg
    def doit(self, msg):
        print(msg)
    def __repr__(self):
        return str(self.msg )+ ' spam object create ho gaya '    # ye wala mai add kiya hu ki object create hu to uska output ache se dekha pau

class Person:
    def __init__(self, name , job=None):
        self.name = name
        self.job = job
    def __repr__(self):
        return 'name = '+ self.name + ' Job = ' + self.job


if __name__ == '__main__':
    obj1 = fact_ory(Spam," my message")   # make spam object
    obj2 = fact_ory(Person, "Arthur", "king")
    obj3 = fact_ory(Person, name = "Brajesh", job = 'None')

    print(obj1)
    print(obj2)
    print(obj3)