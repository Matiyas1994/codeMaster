from collections import defaultdict, deque
def solve():
    security = input()
    key = input()
    dic = {}
    keys = [[0 for k in range(3)] for i in range(3)]
    for i in range(len(key)):
        keys[i//3][i%3] = key[i]
        dic[key[i]] = (i//3, i%3)


    direction = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
    count = 0
    def valid(x,y):
        return 0<= x < 3 and 0<= y < 3
    
    def bfs(mx, my, target):
        queue = deque()
        queue.append((mx, my, 0))
        visited = set()

        while queue:
            cur_x, cur_y, step = queue.popleft()

            if keys[cur_x][cur_y]==target:
                return (step, cur_x, cur_y)

            for x,y in direction:
                new_i = cur_x + x
                new_j =  cur_y + y
                if valid(new_i, new_j) and (new_i, new_j) not in visited:
                    queue.append((new_i, new_j, step+1))
                    visited.add((new_i, new_j))
   
    pos_x, pos_y = dic[security[0]]
    for i in range(1,len(security)):
        ans, pos_x, pos_y = bfs(pos_x, pos_y, security[i])
        count += ans
    
    return count

print(solve())





    


