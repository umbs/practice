N = input()

maps = {'0': [['0', '0'], ['1', '2']],
        '1': [['0', '1'], ['2', '2']],
        '2': [['1', '1']]
       }

seen = {'2': ['1', '1']}

def solve(inp, a, b):
    if seen.get(inp):
        pairs = seen.get(inp)
        a.append(pairs[0][0])
        b.append(pairs[0][1])

