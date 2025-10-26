import sys
from collections import deque

N, M = map(int, sys.stdin.readline().strip().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))
    
distance = [[0] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
    
def bfs(a, b):
    queue = deque()
    queue.append((a,b))
    
    distance[a][b] = 1 
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 밖으로 나가는지 체크
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            # 벽인지 체크
            if maze[nx][ny] == 0:
                continue
            
            # 길(1)이면서, 방문한 적(0)이 없다면
            if maze[nx][ny] == 1 and distance[nx][ny] == 0:
                # 이전 거리 + 1을 새 거리에 저장
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))
                
    return distance[N-1][M-1]
    
print(bfs(0,0))
