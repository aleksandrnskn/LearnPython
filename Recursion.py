def factorial(x):
    if x < 1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))

def fibonacci(n):
	if n<=1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

n = 10
fibo_series = []

for i in range(0,n):
	fibo_series.append(fibonacci(i))
	
print(fibo_series)
