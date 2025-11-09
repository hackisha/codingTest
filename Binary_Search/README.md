```python3
def binary_search(array, target):
    start = 0                # 0번 인덱스부터
    end = len(array) - 1     # 맨 마지막 인덱스까지
    
    # 1. start가 end를 '추월'하기 전까지 반복
    while start <= end:
        
        # 2. '중간'을 '추측'으로 찍는다
        mid = (start + end) // 2 
        
        # 3. '추측'이 정답이면? -> 찾았다!
        if array[mid] == target:
            return mid  # (인덱스 반환)
            
        # 4. '추측'이 정답보다 작으면? (Up!)
        elif array[mid] < target:
            # 중간보다 왼쪽은 다 버린다.
            start = mid + 1 
            
        # 5. '추측'이 정답보다 크면? (Down!)
        else:
            # 중간보다 오른쪽은 다 버린다.
            end = mid - 1
            
    # 6. while문이 끝났는데 못 찾음
    return None # (못 찾음)
