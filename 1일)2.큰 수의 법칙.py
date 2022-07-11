'''
배열의 크기:N 숫자가 더해지는 횟수:M 연속 가능한 횟수: K
ex) [2,4,5,4,6] M=8 K=3
6+6+6 + 5 + 6+6+6 +5 = 46
'''
n, m, k = map(int,input().split()) # n개의 수를 공백으로 구분하여 받기
data = list(map(int,input().split()))

data.sort()
largest = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k): #가장 큰 수 K번 더하기
        if m == 0:
            break
        else:
            result += largest
            m = m-1
    if m==0:
        break
    result += second
    m = m-1

print(result) #단순하게 for문으로 풀었으나 숫자가 커지면 시간 초과 판정임

