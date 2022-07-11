'''
여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
1. 숫자가 쓰인 카드들이 N * M (행렬) 형태로 놓여 있다.
2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다
3. 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다
4. 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를
뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세움

 3 1 2
 4 1 4          -> 세 번째 행을 골랐을 때 승리
 2 2 2

입력 예시)
 3 3
 3 1 2
 4 1 4
 2 2 2
출력 예시) 2
'''

n, m = map(int,input().split())

result = 0
for i in range(n):
    data = list(map(int,input().split()))
    min_v = min(data)
    result = max(result,min_v)

print(result)

'''
2중 반복문 구조

for i in range(n):
    data  = list(map(int,input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    result = max(result,min_value)
'''
