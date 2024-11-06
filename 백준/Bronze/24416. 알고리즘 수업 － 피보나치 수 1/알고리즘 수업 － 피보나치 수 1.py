global count
count = 0

def fibo(x):
    global count
    dp = [1,1]
    for i in range(2,x):
        count += 1
        dp.append(dp[i-1] + dp[i-2])
    return dp[-1]

x = int(input())

print(f'{fibo(x)} {count}')