testdict={'Codingal': 3, 'is': 1, 'best': 2, 'for': 2, 'Coding': 1}
print("the original dictionary:"+ str(testdict))

K=2
res=0
for key in testdict:
    if testdict[key]==K:
        res=res+1

print("Frequency of 2 is:"+str(res))        
