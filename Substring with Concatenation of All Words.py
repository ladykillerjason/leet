def findSubstring(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    ans = []
    n,cnt = len(s),len(words)
    if n<=0 or cnt<=0:return ans
    dic = {}
    for i in range(cnt):
        if words[i] not in dic.keys():dic[words[i]] = 1
        else:dic[words[i]]+=1
    wl = len(words[0])  # wordlength
    for i in range(wl):
        left ,count=i,0
        tdict = {}
        j = i
        while j<=n-wl:
            st = s[j:j+wl]
            if st in dic.keys():
                if st not in tdict:tdict[st] = 1
                else:tdict[st]+=1
                if tdict[st]<=dic[st]:count+=1
                else:
                    while tdict[st]>dic[st]:
                        st1 = s[left:left+wl]
                        if st1 not in tdict:
                            tdict[st1]=-1
                        else:
                            tdict[st1]-=1
                        if tdict[st1]<dic[st1]:count-=1
                        left+=wl
                if count==cnt:
                    ans+=[left]
                    if s[left:left+wl] not in tdict:
                        tdict[s[left:left+wl]]=-1
                    else:
                        tdict[s[left:left+wl]]-=1
                    count-=1
                    left+=wl
            else:
                tdict={}
                count=0
                left=j+wl
            j +=wl
    return ans


def findSubstring2(s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    counts = {}
    for word in words:
        if word not in counts:
            counts[word]=1
        else:
            counts[word]+=1
    indexes = []
    n,num,length = len(s),len(words),len(words[0])

    for i in range(n-num*length+1):
        seen = {}
        j = 0
        while j<num:
            word = s[i+j*length:i+(j+1)*length]
            if word in counts.keys():
                if word not in seen:
                    seen[word] = 1
                else:
                    seen[word] +=1
                if word not in counts:counts[word] = 0
                if seen[word]>counts[word]:break
            else:break
        j+=1
        if j==num:
            indexes+=[i]
    return indexes




if __name__ == '__main__':


    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    res = findSubstring(s,words)
    print(res)