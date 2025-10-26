# BFS
너비우선 탐색

최단거리 찾을 때 사용

## 기본형태
```python
from collections import deque

def bfs(graph, start_node, visited):
    # 1. 큐(deque)를 생성하고 시작 노드 넣음
    queue = deque([start_node])
    
    # 2. 시작 노드를 방문 처리
    visited[start_node] = True
    
    # 3. 큐가 빌 때까지(방문할 노드가 없을 때까지) 반복
    while queue:
        
        # 4. 큐에서 노드를 하나 꺼냄 (가장 먼저 들어온 것).
        v = queue.popleft()
        
        # 5. (필요시) 현재 노드에서 수행할 작업
        print(v, end=' ') # 예: 방문 순서 출력
        
        # 6. 현재 노드(v)와 연결된 모든 이웃 노드(neighbor)를 확인
        for neighbor in graph[v]:
            
            # 7. 만약 이웃 노드를 아직 방문하지 않았다면
            if not visited[neighbor]:
                
                # 8. 이웃 노드를 큐에 넣고
                queue.append(neighbor)
                
                # 9. 방문 처리
                visited[neighbor] = True
```

## 배운거
### deque()
하나의 인자만 받을 수 있음
ex)
```python
queue = deque()

queue.append((a,b)) # 인자 튜플로 넘겨야함
```
### 리스트 컴프리헨션
```python
[[0] * M for _ in range(N)]
```
([0] 리스트 M번 반복 즉, 행 생성) -> N번 반복

[[0] * M for _ in range(N]
