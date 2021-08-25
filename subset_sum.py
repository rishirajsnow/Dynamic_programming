#Subset SUM problem
#11=4+5+2--> its possible to get sum as 11 using a subset of a
a=[4,3,34,5,10,2]
n=len(a)

dp={}
target=11

def f(i,m):
    if(m==0):
        return 0
    elif(i==n-1):
        if (a[i]==m):
            return True
        else:
            return False
    else:
        if((i,m)in dp):
            return dp[(i,m)]
        else:
            inc= a[i] <=m and f(i+1,m-a[i])
            exc=f(i+1,m)
            
            dp[(i,m)]=(inc or exc)
            return dp[(i,m)]
        
print(f(0,11))