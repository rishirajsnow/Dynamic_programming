#min number of perfect square needed to express i
dp={}

def f(i):
    if(i<=0):
        return 0
    else:
        if(i in dp):
            return dp[i]
        else:
            num=1
            ways=[]
            while(num*num<=i):
                ways.append(1+f(i-num*num))
                num=num+1
            dp[i]=min(ways)
            return dp[i]
        
        
        
print(f(101))
print(dp)