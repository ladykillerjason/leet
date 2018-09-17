def minDistance( word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    p1, p2 = 0, 0
    return calculateDistance(word1, word2, p1, p2)


def calculateDistance( word1, word2, p1, p2):
    if p1 >= len(word1):
        if p2 >= len(word2):
            return 0
        else:
            return len(word2) - p2
    if p2 >= len(word2):
        if p1 >= len(word1):
            return 0
        else:
            return len(word1) - p1
    if word1[p1] == word2[p2]:
        return calculateDistance(word1, word2, p1 + 1, p2 + 1)
    else:
        d1 = calculateDistance(word1, word2, p1, p2 + 1)
        d2 = calculateDistance(word1, word2, p1 + 1, p2)
        d3 = calculateDistance(word1, word2, p1 + 1, p2 + 1)
        return 1 + min(d1, d2, d3)
    return 0


if __name__ == '__main__':
    res = minDistance("json",'jack')
    print(res)