def sum(a, b, c):
    return (a+b+c)

def printBoard(xState, oState):
    zero = 'X' if xState[0] else ('O' if oState[0] else 0)
    one = 'X' if xState[1] else ('O' if oState[1] else 1)
    two = 'X' if xState[2] else ('O' if oState[2] else 2)
    three = 'X' if xState[3] else ('O' if oState[3] else 3)
    four= 'X' if xState[4] else ('O' if oState[4] else 4)
    five = 'X' if xState[5] else ('O' if oState[5] else 5)
    six= 'X' if xState[6] else ('O' if oState[6] else 6)
    seven = 'X' if xState[7] else ('O' if oState[7] else 7)
    eight = 'X' if xState[8] else ('O' if oState[8] else 8)
    print("\n")
    print(f"\t{zero} | {one} | {two}")
    print(f"\t--|---|---")
    print(f"\t{three} | {four} | {five}")
    print(f"\t--|---|---")
    print(f"\t{six} | {seven} | {eight}")

def checkwin(xState, oState):
    wins =[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("\nX WON THE GAME")
            return 1
        if(sum(oState[win[0]], oState[win[1]],oState[win[2]])==3):
            print("\nO WON THE GAME")
            return 0
    return -1
    
def dupli_check(xState, oState, value):
    if((xState[value] == 1) and (oState[value] == 1)):
        print("\nPOSITION ALREADY OCCUPIED!!!")
        return 1
    return -1

if __name__ == "__main__":
    xState= [0, 0, 0, 0, 0, 0, 0, 0, 0]
    oState= [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X & 0 for O chance

    i = 1
    print("WELCOME TO THE TIC TAC TOE GAME")
    while(i<=9):
        printBoard(xState, oState)
        if(turn == 1):
            print("\nX's Chance")
            value = int(input("PLEASE ENTER A VALUE IN B/W 0-8: "))
            dup_check = dupli_check(xState, oState, value)
            if(dup_check == 1):
                value = int(input("PLEASE ENTER THE VALUE AGAIN IN B/W 0-8: "))
                xState[value] = 1
            else:
                xState[value] = 1
        else:
            print("\nO's Chance")
            value = int(input("PLEASE ENTER A VALUE IN B/W 0-8: "))
            dup_check = dupli_check(xState, oState, value)
            if(dup_check == 1):
                value = int(input("PLEASE ENTER THE VALUE AGAIN IN B/W 0-8: "))
                oState[value] = 1
            else:
                oState[value] = 1
        cwin = checkwin(xState, oState)
        if(cwin != -1):
            print("MATCHOVER")
            print("\nFINAL BOARD: ")
            printBoard(xState, oState)
            break
        turn= 1-turn
        if((i == 9) and (cwin == -1)):
            print("\nMATCH DRAWN!!")
            print("FINAL BOARD: ")
            printBoard(xState, oState)
            break
        i = 1 + i