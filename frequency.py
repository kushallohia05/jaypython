frequency={'Baby': 3, 'Pranshul': 9, 'Abir': 9, 'Prabhvir': 9, 'Shaurya': 9}
print("the original dictionary:"+ str(frequency))

A=9
res=0
for key in frequency:
    if frequency[key]==A:
        res=res+1

print("Frequency of 9 is:"+str(res))        
