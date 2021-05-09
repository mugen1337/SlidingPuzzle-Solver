import board


def main():
    
    print("input Row : ", end="")
    N = int(input())

    print("input Column : ", end="")
    M = int(input())

    B = board.Board(N, M)

    B.shuffle()

    while not B.isCleared():
        validMove = B.validMovement()
        print("")
        B.out()
        print("")
        print("valid movement : " + validMove)
        print("input movement : ", end="")
        o = input()
        
        if not B.move(o):
            print("input is invalid")
    

    print("")
    B.out()
    print("\nClear !")        

if __name__ == "__main__":
    main()