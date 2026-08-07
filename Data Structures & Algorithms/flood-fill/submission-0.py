class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        direc = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(image), len(image[0])

        q = deque([(sr, sc)])
        visited = set()

        while q:
            r, c = q.popleft()
            image[r][c] = color

            for dr, dc in direc:
                tr = r + dr
                tc = c + dc

                if tr < ROWS and tr >= 0 and tc < COLS and tc >= 0 and image[tr][tc] == orig and (tr, tc) not in visited:
                    visited.add((tr, tc))
                    q.append((tr, tc))
        return image
