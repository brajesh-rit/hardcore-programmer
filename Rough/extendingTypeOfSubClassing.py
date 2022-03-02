from __future__ import print_function

class Set(list):
    def __int__(self, val = []):          #construction
        list.__init__(self)              # call list constructor
        self.concat(val)                 # copy mutable defaults
    def intersect(self, other):
        res = []
        for x in self:
            if x in other:              # pick common items
                res.append(x)
        return Set(res)                 # list banak apne app class me hi paas kare apna object return kara diya
    def union(self, other):
        res = Set(self)
        res.concat(other)               # concat method baad me define kiya hai lekin phir isko call kar sakte hai
        return res
    def concat(self, value):
        for x in value:
            if not x in self:
                self.append(x)
    def __and__(self,other): return self.intersect(other)     # yeha per operator overloading kiya gaya hai
    def __or__(self,other):  return self.union(other)
    def __repr__(self):  return 'sets: ' + list.__repr__(self)

if __name__ == '__main__':
    x = Set([1,3,5,7])
    y = Set([2,1,4,5,6])

    print (x, y, len(x))
    print (x.intersect(y), y.union(x))
    print (x & y, y|x)
    x.reverse()
    print(x)