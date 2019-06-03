'''
A recursive program to test whether a given string can be segmented into space
separated words in dictionary

Geeksforgeeks: https://www.geeksforgeeks.org/word-break-problem-dp-32/
DP Solution: https://www.techiedelight.com/word-break-problem/
'''

dictionary = ["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"]

def wordBreakRecursive(string, result):

    # Base case
    if (len(string) == 0):
        print(result)
        return

    # Try all prefixes of lengths from 1 to size
    for i in range(1, 1+len(string)):
        if (string[0:i] in dictionary):
            result.append(string[0:i])
            wordBreakRecursive(string[i:], result)
            result.pop()

    return


# Driver program to test above functions
if __name__ == "__main__":
    result = []
    wordBreakRecursive("ilikesamsung", result)
    print("###########")
    wordBreakRecursive("iiiiiiii", result)
    print("###########")
    wordBreakRecursive("", result)
    print("###########")
    wordBreakRecursive("ilikelikeimangoiii", result)
    print("###########")
    wordBreakRecursive("samsungandmango", result)
    print("###########")
    wordBreakRecursive("samsungandmangok", result)
    print("###########")
