#토마토

from collections import deque

M, N = map(int, input().split())

box = [] 
distance = []

for _ in range(N):
    box.append(list(map(int, input().split())))

distance = [[0]*M for _ in range(N)]

queue = deque()
for a in range(N):
    for b in range(M):
        if box[a][b] == 1:
            queue.append((a,b))
        if box[a][b] == 0:
            distance[a][b] = -1


dx = [1, -1, 0 ,0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if distance[nx][ny] == -1:
                distance[nx][ny]= distance[x][y] + 1
                queue.append((nx,ny))
        
    answer = 0
    for i in range(N):
        for j in range(M):
            if distance[i][j] == -1:
                return -1
            answer = max(answer, distance[i][j])
    
    return answer

            
print(bfs())



