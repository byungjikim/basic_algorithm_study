'''
배열의 크기:N 숫자가 더해지는 횟수:M 연속 가능한 횟수: K
ex) [2,4,5,4,6] M=8 K=3
6+6+6 + 5 + 6+6+6 +5 = 46

수학적 접근: 가장 큰 수, 두 번째로 큰 수 찾기는 같음

M을 K+1만큼 나눈 몫 = 수열을 반복하는 횟수
K+1로 나눠지지 않는 경우는 위의 식의 나머지만큼 가장 큰 수가 더해짐
가장 큰 수가 더해지는 횟수 => int(m / (k+1)) *k + m%(k+1)
예시의 경우 8/4 = 2 이므로 2번 반복이고 k가 이 수열에 3개씩 할당되었으므로 *k
6개 있고 나머지는 0임
'''
n,m,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k + m%(k+1)

result =0
result += count * first
result += (m-count) * second

print(result)
