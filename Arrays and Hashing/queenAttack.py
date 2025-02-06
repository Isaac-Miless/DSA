class Solution:
    def queenAttack(self, queen: list[int], opp: list[int]) -> None:
        # queen: [x, y]
        # opp: [x, y]
        if queen[0] == opp[0] or queen[1] == opp[1] or abs(queen[0] - opp[0]) == abs(queen[1] - opp[1]):
            print('Can Attack')
