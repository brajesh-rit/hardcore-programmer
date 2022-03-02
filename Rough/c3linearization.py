class A: pass
class B: pass
class C(A,B): pass
class D(B,A): pass
class E(C,D): pass  # This line return error Cannot create a consistent method resolution order (MRO) for bases A, B
                    # Because class C ,D inheritance  A,B  and B,C  which is confusing

if __name__ == '__main__':
    D.mro()
