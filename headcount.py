import sys

text = "".join(sys.stdin.read().splitlines())
rows = text.replace("[", "").split("]")
grid = [[x.strip() for x in line.split(",")] for line in rows]
grid = [[x for x in line if x] for line in grid]
grid = [line for line in grid if line]
grid = [[bool(int(x)) for x in line] for line in grid]

R, C = len(grid), len(grid[0])
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
team = [[0] * C for _ in range(R)]

def dfs(sx, sy, mark):
    team_size = 1
    team[sy][sx] = mark
    q = [(sx, sy)]
    while q:
        x, y = q.pop()
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] and not team[ny][nx]:
                team[ny][nx] = mark
                team_size += 1
                q.append((nx, ny))
    return team_size

team_sizes = []
for sy in range(R):
    for sx in range(C):
        if not grid[sy][sx] or team[sy][sx]:
            continue
        team_sizes.append(dfs(sx, sy, len(team_sizes) + 1))
team_sizes.sort(reverse=True)

print(f"{len(team_sizes)} teams of {team_sizes} totaling {sum(team_sizes)}")
