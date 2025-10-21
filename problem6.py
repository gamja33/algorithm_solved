import sys
input = sys.stdin.readline

def heapify(arr, n, heap_size):
    largest = n
    left = 2 * n
    right = 2 * n + 1

    if left <= heap_size and arr[left] > arr[largest]:
        largest = left
    if right <= heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != n:
        arr[n], arr[largest] = arr[largest], arr[n]
        heapify(arr, largest, heap_size)

def build_heap(arr):
    heap_size = len(arr) - 1
    for i in range(heap_size // 2, 0, -1):
        heapify(arr, i, heap_size)
    return arr

def heap(arr):
    arr = [0] + arr 
    build_heap(arr)

    heap_size = len(arr) - 1

    for i in range(heap_size, 1, -1):
        arr[1], arr[i] = arr[i], arr[1]
        heapify(arr, 1, i-1)

    return arr[1:]
N = int(input()) #영화의 갯수
time_list = [] #영화 시간 list
for _ in range(N):
    start_time, end_time = map(int, input().split()) #map함수로  2개의 값에 각각 받음
    time_list.append((end_time, start_time)) #튜플형태로 저장


time_list = heap(time_list) #힙정렬로 정렬 
result_count = 0 #총 영화를 상영 할 수 있는 수
last_finish_time = 0 #마지막으로 끝난 영화시간
for end, start in time_list:
    if start >= last_finish_time: #마지막 영화시간보다 크다면
        result_count += 1 #상영시간이 겹치지 않음으로 count +1 
        last_finish_time = end #마지막 영화시간 갱신
print(result_count)