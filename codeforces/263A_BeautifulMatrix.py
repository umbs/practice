def Beautiful_Matrix():
    for r in range(5):
        s = raw_input().find('1')
        if s != -1:
            print abs(2-s/2) + abs(2-r)
            return
    return


if __name__ == "__main__":
    Beautiful_Matrix()
