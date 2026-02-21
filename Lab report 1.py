class Node:
    def __init__(self, x, y, level, path):
        self.x = x
        self.y = y
        self.level = level
        self.path = path


class IDDFS:
    def __init__(self):
        self.moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def init(self):
        n, m = map(int, input().split())

        grid = []
        for _ in range(n):
            grid.append(list(map(int, input().split())))

        sx, sy = map(int, input("Start: ").split())
        gx, gy = map(int, input("Target: ").split())

        max_depth = n * m

        found = False
        final_depth = 0
        final_path = []

        for limit in range(max_depth + 1):
            result = self.dls(grid, sx, sy, gx, gy, limit, n, m)
            if result:
                found = True
                final_depth = result[0]
                final_path = result[1]
                break

        if found:
            print(f"Path found at depth {final_depth} using IDDFS")
            print(f"Traversal Order: {final_path};")
        else:
            print(f"Path not found at max depth {max_depth} using IDDFS")

    def dls(self, grid, sx, sy, gx, gy, limit, n, m):
        stack = [Node(sx, sy, 0, [(sx, sy)])]
        visited = set()

        while stack:
            node = stack.pop()

            if node.x == gx and node.y == gy:
                return node.level, node.path

            if node.level < limit:
                for dx, dy in self.moves:
                    nx = node.x + dx
                    ny = node.y + dy

                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] == 0 and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            stack.append(
                                Node(nx, ny, node.level + 1,
                                     node.path + [(nx, ny)])
                            )

        return None


if __name__ == "__main__":
    iddfs = IDDFS()
    iddfs.init()