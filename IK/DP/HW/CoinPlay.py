'''
https://algorithms.tutorialhorizon.com/dynamic-programming-coin-in-a-line-game-problem/

Understood the solution from above link
'''
def maxWin_nonDP(v):
    if len(v) == 0:
        return 0

    if len(v) == 1:
        return v[0]

    # If player A chooses 1st coin, opponent B tries to choose in such a way
    # that player A's collection is minimum (B is thinking ahead too)
    a = v[0] + min(maxWin(v[2:]), maxWin(v[1:-1]))
    b = v[-1] + min(maxWin(v[1:-1]), maxWin(v[:-2]))

    return max(a, b)


if __name__ == "__main__":
    print(maxWin_nonDP([8, 15, 3, 7]))
