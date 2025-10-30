#불!
from collections import deque

R, C = map(int, input().split())

maze = []

for _ in range(R):
    maze.append(list(input()))
    

fire = [[-1]*C for _ in range(R)]

jihoon = [[-1]*C for _ in range(R)]

dx = [0,0, 1, -1]
dy = [1, -1 ,0 ,0]

queue_fire = deque()
queue_jihoon = deque()

for i in range(R):
    for k in range(C):
        if maze[i][k] == 'F':
            fire[i][k] = 0
            queue_fire.append((i, k))
        if maze[i][k] == 'J':
            jihoon[i][k] = 0
            queue_jihoon.append((i, k))
            
            
def bfs_fire():
    while queue_fire:
        x, y = queue_fire.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if maze[nx][ny] == '#':
                continue
            if fire[nx][ny] == -1:
                queue_fire.append((nx,ny))
                fire[nx][ny]=fire[x][y] + 1
            

    
def bfs_jihoon():
    while queue_jihoon:
        x, y = queue_jihoon.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                print(jihoon[x][y]+1)
                return
            if maze[nx][ny] == '#' or jihoon[nx][ny] != -1:
                continue
            if fire[nx][ny] != -1 and (jihoon[x][y] + 1)>= fire[nx][ny]:
                continue
            jihoon[nx][ny] = jihoon[x][y] + 1
            queue_jihoon.append((nx,ny))
            
    print("IMPOSSIBLE")
    
    

bfs_fire()
bfs_jihoon()
