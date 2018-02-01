'''@author: Alex Waweru'''
'''Ancient Roman Mathematics Operations'''

def add(No1, No2):
    total = No1+No2
    print(total)
    return _standardize(total)

def _standardize(No):
    ans = ''
    for i in range(len(No)):
        min_idx = i
        for j in range(i+1, len(No)):
            if _romanToDecimal(No[min_idx]) < _romanToDecimal(No[j]):
                min_idx = j
        ans=ans + No[min_idx]
    return ans
        
def multiply(No1, No2):
    a=a


def romanToDecimal(No):
    ans = 0
    i = 0
    while (i<len(No)):
        if i+1 < len(No):
            if _romanToDecimal(No[i])>=_romanToDecimal(No[i+1]):
                ans = ans+_romanToDecimal(No[i])
                i=i+1
            else:
                ans = ans+_romanToDecimal(No[i+1])-_romanToDecimal(No[i])
                i=i+2
        else:
            ans = ans+_romanToDecimal(No[i])
            i=i+1
    return ans
            
        
    
    

def _romanToDecimal(L):
    romans = ['I','V','X','L','C','D','M']
    values = [1,5,10,50,100,500,1000]
    val = 0
    for i in range(len(romans)):
        if L == romans[i]:
            val = values[i]
    return val
        
    
    
    
