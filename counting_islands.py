from collections import defaultdict


def dfs(i, j, grid, visited, count, islands):
    if (i, j) in visited:
        return
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return
    if grid[i][j] == 0:
        return
    visited.add((i, j))
    islands[count].append((i, j))
    dfs(i, j + 1, grid, visited, count, islands)
    dfs(i + 1, j, grid, visited, count, islands)
    dfs(i, j - 1, grid, visited, count, islands)
    dfs(i - 1, j, grid, visited, count, islands)


if __name__ == '__main__':
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    count1 = 0
    visited1 = set()
    islands1 = defaultdict(list)
    count2 = 0
    visited2 = set()
    islands2 = defaultdict(list)
    for i, row in enumerate(grid1):
        for j, col in enumerate(row):
            if col == 1 and (i, j) not in visited1:
                count1 += 1
                dfs(i, j, grid1, visited1, count1, islands1)

    for i, row in enumerate(grid2):
        for j, col in enumerate(row):
            if col == 1 and (i, j) not in visited2:
                count2 += 1
                dfs(i, j, grid2, visited2, count2, islands2)

    count = 0
    for island in islands2.values():
        flag = True
        for land in island:
            if grid1[land[0]][land[1]] == 0:
                flag = False
                break
        if flag:
            count += 1
    print(count)