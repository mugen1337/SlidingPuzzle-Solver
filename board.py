import copy
import random

# todo : add assert
# generate N * M board
class Board:
    def __init__(self, N, M):
        # params
        self.N = N
        self.M = M
        self.E = N * M - 1 # empty cell

        # board initialize 0 ~ N*M-1
        self.board = [[0 for i in range(M)] for j in range(N)]
        for i in range(N):
            for j in range(M):
                self.board[i][j] = i * M + j

    def correctNumber(self, i, j):
        return i * self.M + j
    
    def correctPosition(self, num):
        return (num // self.M, num % self.M)

    def dis(self, ai, aj, bi, bj):
        return abs(ai - bi) + abs(aj - bj)

    # Can be current board cleared?
    # ref : https://manabitimes.jp/math/979
    def isFeasible(self):
        cnt = [0 for i in range(self.N * self.M)]
        for i in range(self.N):
            for j in range(self.M):
                if not (0 <= self.board[i][j] and self.board[i][j] < self.N * self.M):
                    return False
                cnt[self.board[i][j]] += 1
                if cnt[self.board[i][j]] > 1:
                    return False

        b = copy.deepcopy(self.board)
        swapCnt = 0
        for i in range(self.N):
            for j in range(self.M):
                if self.correctNumber(i, j) == b[i][j]:
                    continue
                
                swapCnt += 1
                for k in range(self.N):
                    for l in range(self.M):
                        if self.correctNumber(i, j) == b[k][l]:
                           b[i][j], b[k][l] = b[k][l], b[i][j]

        disE = 0
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == self.E:
                    disE = self.dis(i, j, self.N - 1, self.M - 1)
        
        return (swapCnt % 2) == (disE % 2)
    
    # to be improved
    # i think this program is not good enough
    def shuffle(self):
        def generateRandomly():
            b = list(range(self.N * self.M))
            random.shuffle(b)
            c = [[0 for i in range(self.M)] for j in range(self.N)]
            for i in range(self.N):
                for j in range(self.M):
                    c[i][j] = b[i * self.M + j]
            return c

        self.board = generateRandomly()
        while not self.isFeasible():
            self.board = generateRandomly()

    def isCleared(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.correctNumber(i, j) != self.board[i][j]:
                    return False
        return True

    # Movement
    # R : move the piece which is on the light of empty cell to right
    def validMovement(self):
        ret = ""
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == self.E:
                    i_E = i
                    j_E = j

        if j_E != self.M-1:
            ret += "L"
        if j_E != 0:
            ret += "R"
        if i_E != self.N-1:
            ret += "U"
        if i_E != 0:
            ret += "D"
        
        return ret

    # o : LRUD
    def isValidMovement(self, o):
        if (len(o) != 1) or (not o in self.validMovement()):
            return False
        return True

    def move(self, o):
        if not self.isValidMovement(o):
            return False

        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == self.E:
                    i_E = i
                    j_E = j

        if o == "L":
            self.board[i_E][j_E], self.board[i_E][j_E + 1] = self.board[i_E][j_E + 1], self.board[i_E][j_E]
        if o == "R":
            self.board[i_E][j_E], self.board[i_E][j_E - 1] = self.board[i_E][j_E - 1], self.board[i_E][j_E]
        if o == "U":
            self.board[i_E][j_E], self.board[i_E + 1][j_E] = self.board[i_E + 1][j_E], self.board[i_E][j_E]
        if o == "D":
            self.board[i_E][j_E], self.board[i_E - 1][j_E] = self.board[i_E - 1][j_E], self.board[i_E][j_E]

        return True
    
    def out(self):
        for i in range(self.N):
            for j in range(self.M):
                if self.board[i][j] == self.E:
                    print(" " * 3, end="")
                else:
                    print("{:>3}".format(self.board[i][j]), end="")
            print("")

    def toString(self):
        ret = ""
        for i in range(self.N):
            for j in range(self.M):
                ret += str(self.board[i][j]) + " "
        return ret