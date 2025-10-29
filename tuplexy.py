def palind(r):
    e=len(r)-1
    s=0
    while(s<e):
            if(r[s]!=r[e]):
                    return False
            s+=1
            e-=1
    return True
r=(1,2,3,3,2,2)

if(palind(r)):
       print("The tuple is  Flip-flop")
else:
       print("THE TUPLE IS NOT FLIP-FLOP")       