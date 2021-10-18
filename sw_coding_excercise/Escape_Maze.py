'''
미로 탈출

동빈이는 N × M 크기의 직사각형 형태의 미로에 갇혔다. 미로에는 여러 마리의 괴물이 있어 이를 피해 탈출해야 한다.
동빈이의 위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
이 때, 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다.
이 때, 동빈이가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하라. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.

<입력>
* 첫째 줄에 두 정수 N, M (4 <= N, M <= 200)이 주어진다.
* 다음 N개 중에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
* 각각의 수들은 공백없이 붙어서 입력으로 제시된다. 
* 또한 시작칸과 마지막 칸은 항상 1이다.

5 6
101010
111111
000001
111111
111111

<출력>
첫째줄에 최소 이동 칸의 개수를 출력한다.

10

'''

from collections import deque

# 미로 맵 가로길이 n, 세로길이 m 을 입력
n, m = map(int, input().split())

maze = []
for i in range(n):
  maze.append(list(map(int, input())))
print(maze)

'''
<출력>
101010
111111
000001
111111
111111

[[1, 0, 1, 0, 1, 0],
 [1, 1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 1],
 [1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1]]

'''
# 상, 하, 좌, 우 좌표(인덱스) 정의 설정
# 상:(0,-1), 하:(0,1), 좌:(-1,0), 우:(1,0)
dx = [0,0,-1,1]
dy = [-1,1,0,0]
maze_copy = maze.copy()
# 미로맵에서 움직인 좌표 숫자 카운트
def move(x, y):
  queue = deque()             # 빈 deque 리스트 생성
  queue.append((x, y))        # 빈 deque 리스트에 (x, y) 튜플 좌표 입력
  while queue:                # queue 리스트 안에 변화 입력된 내용을 가지고 반복적으로 반복문 수행
    x, y = queue.popleft()    # queue 리스트 안의 튜플값 요소를 꺼내서 x, y 변수에 입력
    
    for i in range(4):        # 상,하,좌,우 4방향으로 주변 요소값을 확인
      nx = x + dx[i]
      ny = y + dy[i]
      
      # 미로맵 공간 자체를 조금이라도 벗어나면 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      
      # 미로맵 위의 값 괴물(0)을 만나는 경우 무시
      if maze_copy[nx][ny] == 0:
        continue
      
      # 미로맵 위의 값 1을 만나는 경우 카운트
      if maze_copy[nx][ny] == 1:
        maze_copy[nx][ny] = maze_copy[x][y] + 1  # 현(x,y)좌표 해당값에 카운트값 1을 추가로 더해서 (nx,ny)주변좌표 해당값에 덮어쓰기함  
        queue.append((nx, ny))                   # queue 튜플 리스트에 nx,ny 값을 덮어쓰기하여 맨 위로 다시 반복수행
  
  return maze_copy[n-1][m-1]     # 미로맵의 맨 오른쪽 끝단 (n-1,m-1)좌표 해당 입력값을 반환

print(move(0,0))
maze_copy

'''
<출력>
10

[[3, 0, 5, 0, 7, 0],
 [2, 3, 4, 5, 6, 7],
 [0, 0, 0, 0, 0, 8],
 [14, 13, 12, 11, 10, 9],
 [15, 14, 13, 12, 11, 10]]
'''
