'''
N이 1이 될 떄까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행한다
1. N-1
2. N/K (단 N이 K로 나누어 떨어질 때만 가능하다)

ex) N= 17 , K= 4 인 경우에 1번 수행 : N= 16 // 2번을 두 번 수행 : N=1
N K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야하는 최소 횟수를
구하는 프로그램
입력 예시) 25 5
출력 예시) 2
'''
n, k = map(int, input().split())
result = 0

while n>= k:
    while n%k !=0: #n이 k로 나누어 떨어지지 않으면 -1 반복
        n -=1
        result +=1
    n= n//k
    result +=1

while n>1: #위의 경우에서 n이 1이나오면 건너뛰는 것이고 
    n -=1  #n이 k보다 작은데 1이 아닌 경우 실행 1씩 빼서 1로 
    result +=1
print(result)

#숫자 크기가 작으니까 1씩 컨트롤 한건데 커지면 너무 오래걸림

'''
while True:
    target = (n//k) * k  #나눠지는 만큼의 수
    result += (n - target) # result에 나머지를 넣음 나머지만큼 -1 연산 하므로
    n= target #n 에는 나눠지는 만큼의 수를 넣음
    if n < k: #더이상 못나눌 때 탈출
        break
    result +=1 #나눌 수 있을 때 나누고 +1
    n = n//k

result += (n-1) # 1을 남겨야 하므로 연산 작업이 n번이면 0
'''
