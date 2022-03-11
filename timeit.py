'''
Inderpreet Singh
CMPE-131 Sec 02
HW2 - Q3
'''
import time

# Decorator
def calculate_time(func):
    
    def inner_time():
        
        # Store start time
        begin = time.time()

        func()
    
        # Store end time
        end = time.time()

        print("Total time ",end - begin)
    return inner_time
  
@calculate_time
def on_time():
    print('time!')
on_time()
