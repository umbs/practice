def solve(arr):
    # (k, [count, highest_value])
    res = dict()

    for s in arr:
        k, v = s.split()
        if k in res:
            count, old_str = res[k]
            res[k] = [count+1, max(v, old_str)]
        else:
            res[k] = [1, v]


    out = list()
    for k, v in res.items():
        out.append(''.join(k + ':' + str(v[0]) + ',' + v[1]))

    return out


if __name__ == "__main__":
    # arr = ['mark zuckerberg', 'tim cook', 'mark twain']
    arr = ['key1 abcd', 'key2 zzz', 'key1 hello', 'key3 world', 'key1 hello']
    print(solve(arr))
