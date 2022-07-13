# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
n,m = map(int, input().split())

# initialize N*M map
d = [ [0] * m for _ in range(n)]

# current coordinate & direction of the character
x, y, direction = map(int, input().split())
d[x][y] = 1 # current coordinate > visit status

# information of map (land or sea)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# define North, East, South, West
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# turn to the left
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# simulation
count = 1 # the current coordinate
turn_time = 0
while True:
    turn_left()
    
    #coordinate to be moved
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
        
    # all directions are non-m
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        # possible to move backward
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # the back is the sea
        else:
            break
        turn_time = 0

print(count)
        
