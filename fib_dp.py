dp={}

def f(n):
    if n==1 or n==2:
        return 1
    else:
        if n in dp:
            return dp[n]
        else:
            dp[n]=f(n-1)+f(n-2)
            return dp[n]

for i in range(1,5):
    print(i,f(i))