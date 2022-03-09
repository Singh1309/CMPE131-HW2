'''
Inderpreet Singh
CMPE-131 Sec 02
HW2 - Q1
'''
def sort_list(myList):
    
    n = len(myList)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if myList[j] > myList[j+1] :
                myList[j], myList[j+1] = myList[j+1], myList[j]
                
    return myList

print('Output = ', sort_list([-1,-3.9,7]))
print('Output = ', sort_list([11,2,4,99]))
