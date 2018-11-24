def towers_of_hannoi(n, src, dst, aux):
    '''
    Instructor's solution
    '''
    if n == 1:
        print("Move disk 1 from " + src + " to " + dst)
        return

    towers_of_hannoi(n-1, src, aux, dst)
    print("Move disk " + str(n) + " from " + src + " to " + dst)
    towers_of_hannoi(n-1, aux, dst, src)


if __name__ == "__main__":
    towers_of_hannoi(2, "T1", "T2", "AUX")
