'''
Inderpreet Singh
CMPE-131 Sec 02
HW2 - Q4
'''

def doubler(func):         # decorator definition
    def twice():
        func()
        func()
    return twice

@doubler
def whee():             # testing function
    print('whee')
whee()
