"""
Below sricpt for testing the print reverse and forward printing
only one statement "sending insertion to print"
change the behaviour of program
"""
def print_rec(n):
    if (n == 1):
        print(n)
        return
    print_rec(n-1)    # this program print increment number 1,2,3,4.......
    print(n)         #only this statement move before hypothesis it print opposite direction

print_rec(10)

def print_rec(n):
    if (n == 1):
        print(n)
        return
    print(n)        #this program print decrement number  10,9,8,7 .....
    print_rec(n-1)

print_rec(10)