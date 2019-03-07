'''
A recursive program to test whether a given string can be segmented into space
separated words in dictionary

Geeksforgeeks: https://www.geeksforgeeks.org/word-break-problem-dp-32/
'''

dictionary = ["mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"]

def wordBreakRecursive(string, result):

    # Base case
    if (len(string) == 0):
        return True;

    # Try all prefixes of lengths from 1 to size
    for i in range(1, 1+len(string)):
        if (string[0:i] in dictionary):
            result.append(string[0:i])
            if wordBreak(string[i:], result): 
                return True;
            else:
                return False
            result.pop()

    return False;


# Driver program to test above functions
if __name__ == "__main__":
    result = []
    # if wordBreak("ilike", result):
    if wordBreak("ilikesamsung", result):
        print("Yes")
    else: 
        print("No")
    
    ''' 
    wordBreak("iiiiiiii")
    wordBreak("")
    wordBreak("ilikelikeimangoiii")
    wordBreak("samsungandmango")
    wordBreak("samsungandmangok")
    ''' 
