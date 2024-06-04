N = int(input())
from math import log
n = log(N//3,2)

lines = []
def draw(n):
    
    ans = []
    if n == 0:
        ans.append('  *  ')
        ans.append(' * * ')
        ans.append('*****')
        return ans
    else:
        temp = draw(n-1)
        pad = ' '*(len(temp[0])//2+1)
       
        # 1) 기존부분 padding
        # 2) 새로운 부분         
        for i in range(len(temp)):
            temp.append(temp[i] + ' ' + temp[i])
            temp[i] = pad + temp[i] + pad
        return temp

result = draw(n)
print('\n'.join(result))