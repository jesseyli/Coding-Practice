import math

def removeConsecutive(string):
    current = None
    final = ""
    for i in string:
        if i != current:
            final += i
        current = i
   	return final
            
def numberOfActions(number):
    if number == 0:
        return 0
    if number == 1:
    	return 1
    return len(bin(number)) - 1

'''
N = len(p)
counter = 0
total = math.pow(2,N)
while counter < total:
    
    counter += 1
'''
