# 재귀 안쓰고 구현 -> 맞음!

arr = [0, 1]
length = int(input())
idx = 2
while len(arr) <= length:
    arr.append((arr[idx-2] + arr[idx-1]))
    idx += 1

print(arr[length])


# 재귀 도전
def fibo(stop, current, x, y):
    if stop == current:
        return x + y
    else:
        current += 1
        fibo(stop, current, y, x+y)

print(fibo(10, 2, 0, 1))


# 재귀 사용한 풀이 - 시간초과

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))


# 일반 풀이

n = int(input())

a, b = 0, 1

while n > 0:
    a, b = b, a + b  #초간단한 저장이네..
    n -= 1           #오 횟수를 이렇게 세냐..

print(a)