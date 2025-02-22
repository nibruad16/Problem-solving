# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

import math

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m = len(img)
        n = len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                for x in range(max(0, i - 1), min(m, i + 2)):
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        total += img[x][y]
                        count += 1

                result[i][j] = math.floor(total / count)

        return result