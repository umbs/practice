def happyNumber(N):
    orig = N
    seen = {N}
    while True:
        res = 0
        while N:
            r = N%10
            res += r * r
            N = N//10

        if res == 1:
            # print("%s is Happy" % orig)
            return True
        elif res in seen:
            # print("%s is Sad" % orig)
            return False
        else:
            seen.add(res)
            N = res

if __name__ == "__main__":
    happy = []
    for i in range(100):
        if happyNumber(i):
            happy.append(i)

    print(happy)
