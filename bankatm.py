#Bank ATM problem
#13=7+6 -->2 
dp={}
a=[2,7,1,6]

def f(i):
    if (i<=0):
        return 0
    else:
        if i in dp:
            return dp[i]
        else:
            num=0
            ways=[]
            while(num<len(a)):
                ways.append(1+f(i-a[num]))
                num=num+1
            dp[i]=min(ways)
            return dp[i]
print(f(13))
print(dp)