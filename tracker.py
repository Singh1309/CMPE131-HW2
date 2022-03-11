'''
Inderpreet Singh
CMPE-131 Sec 02
HW2 - Q5
'''

def func_counter(func):
    def inner(*args, **kwargs):
        inner.counter += 1
        return func(*args, **kwargs)
    inner.counter = 0
    return inner

@func_counter
def foo(y):
    return y+2**3 - 34

print(foo(3))
print(foo(34))
print(foo.counter)
