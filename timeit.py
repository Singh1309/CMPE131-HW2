'''
Inderpreet Singh
CMPE-131 Sec 02
HW2 - Q3
'''
import time

# Decorator
def calculate_time():
    
    # Store start time
    begin = time.time()

    time.sleep(3) # For testing
    
    # Store end time
    end = time.time()

    print("Total time ",end - begin)
  
calculate_time()
