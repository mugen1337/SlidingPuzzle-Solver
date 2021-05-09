import copy
import heapq

from board import *

# heuristic, sum of manhattan distance
def costH(board):
    ret = 0
    for i in range(board.N):
        for j in range(board.M):
            to = board.correctPosition(board.board[i][j])
            ret += board.dis(i, j, to[0], to[1])
    return ret;

# ref : https://qiita.com/Darsein/items/749f3b352cfaa22f9f28
# O((N*M)^2)
def boardHash(B):
    P = []
    for w in B:
        for x in w:
            P.append(x)
    N = len(P)
    v = [0 for i in range(N)] # inversion vector
    for i in range(N):
        for j in range(i+1, N):
            if P[i] > P[j]:
                v[i] += 1
    mul = 1
    ret = 0
    for i in range(N):
        ret += v[N - 1 - i] * mul
        mul *= i + 1
    return ret

def solve(board):
    que = []
    heapq.heapify(que)

    pool = []
    boardToIdx = {}
    
    cost = []
    prev = []

    costIni = 0 + costH(board)
    cost.append(costIni)
    prev.append((-1, -1))
    heapq.heappush(que, (costIni, 0, 0)) # (steps + costH, steps, index)
    boardToIdx[boardHash(board.board)] = 0
    pool.append(copy.deepcopy(board))

    while len(que) > 0:
        costSum, steps, idx = heapq.heappop(que)

        if cost[idx] < costSum:
            continue

        if pool[idx].isCleared():
            break

        for o in pool[idx].validMovement():
            nxt = copy.deepcopy(pool[idx])
            nxt.move(o)
            
            h = boardHash(nxt.board)

            if h in boardToIdx:
                to = boardToIdx[h]
            else:
                to = len(cost)
                boardToIdx[h] = to
                cost.append(1e15)
                prev.append((-1, -1))
                pool.append(copy.deepcopy(nxt))
            
            costTo = steps + 1 + costH(nxt)

            if costTo < cost[to]:
                cost[to] = costTo
                prev[to] = (idx, o)
                heapq.heappush(que, (costTo, steps + 1, to))

    clearedB = Board(board.N, board.M)
    p = boardToIdx[0]
    res = ""
    while p != 0:
        res += prev[p][1]
        p = prev[p][0]
    res = res[::-1]
    return res

def main():
    print("--------------------------------------------------------")
    print("Input Board")
    print("1. enter number of Row and Column")
    print("2. enter board")
    print("   if enter -1, then it will be treated as empty cell")
    print("")
    print("(example)")
    print("input Row : 3\ninput Column : 3\ninput row 1 : 6 0 7\ninput row 2 : 2 5 -1\ninput row 3 : 1 4 3")
    print("--------------------------------------------------------")

    print("input Row : ", end="")
    N = int(input())

    print("input Column : ", end="")
    M = int(input())

    board = Board(N, M)
    for i in range(N):
        print("input row {} : ".format(i+1), end="")

        li = list(map(int, input().split()))
        for j in range(M):
            board.board[i][j] = (li[j] if li[j] >=0 else board.E)
    
    if not board.isFeasible():
        print("invalid board")
        return
    
    print("...")
    
    res = solve(board)

    print("Operations : ", res)


if __name__ == "__main__":
    main()
