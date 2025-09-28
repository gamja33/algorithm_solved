def bubble_sort(arr:list) ->list:
    """버블정렬"""
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] =  arr[j+1], arr[j]    
    return arr


print("[입력_largest값]")
N, M, K = map(int, input().split()) #N=수열갯수, M=더하는횟수 K=연속 제한 값

arr = list(map(int, input().split())) #공백을 기준으로 리스트 생성
arr = bubble_sort(arr)


largest  = arr[0] #최댓값
second_largest = arr[1] #2번째로 큰 값



count = (M // (K + 1)) * K + (M % (K + 1)) #최댓값 반복수

# 만족하는 제일 큰 수를 나타내기 위해서는 가장 큰수 K번 과 다음 큰 수 1번이 한 싸이클
# (M // (K+1))*K <- 최대 사이클 수, (M % (K + 1)) <- 사이클 하고 남은 수
# (M % (K + 1)) <- 사이클 하고 남은 수 (최댓값만 더하면 됨)

result = count * largest #가장 큰 수가 더해지는 총합
result += (M - count) * second_largest #두번째로 큰 값이 더해지는 총합

print("[출력값]")
print(result)
