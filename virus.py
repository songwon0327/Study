def check(start,arr,visited):
    visited.append(start)
    for j in range(computer+1):
        if arr[start][j] == 1 and j not in visited:
            visited = check(j,arr,visited)
    return visited        

computer = int(input())
line = int(input())
arr = [[0 for col in range(computer+1)] for row in range(computer+1)]
visited = []

for i in range(line):
    x, y = map(int,input().split())
    arr[x][y] = 1
    arr[y][x] = 1
    
print(len(check(1,arr,visited))-1)