class Solution:
    def kingMove(self, king: list[int], dest: list[int]) -> int:
        # king: [x, y]
        # dest: [x, y]
        return max(abs(king[0] - dest[0]), abs(king[1] - dest[1]))
