def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    dic ={}
    for i in range(128):dic[i] = 0
    for i in t:dic[ord(i)] += 1  # t中每个字符对应的数目，即还没有找到的个数
    counter = len(t);begin=0;end=0;d=9999999;head=0
    while end < len(s):
        if dic[ord(s[end])]>0:counter -=1
        dic[ord(s[end])]-=1;end+=1 # 如果在t中，则只是普通的减一，否则end位将变为负数,与下面begin判断对应
        while counter==0: # 已经把t中所有的字符都取完了
            if end-begin<d:head=begin;d=end-head
            if dic[ord(s[begin])]==0:counter+=1 # 如果begin字符在t中，则将其除去，所以counter需要加一
            dic[ord(s[begin])]+=1;begin+=1
    return "" if d==9999999 else s[head:head+d]




if __name__ == '__main__':

    S = "ADOBECODEBANC"
    T = "ABC"
    res = minWindow(S,T)
    print(res)
