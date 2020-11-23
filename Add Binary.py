def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if len(b)>len(a):a,b=b,a
    b = '0'*(len(a)-len(b))+b
    res = ['0' for i in range(len(a)+1)]
    carry = 0
    j = -1
    for i in range(len(a)):
        tmp = int(a[j])+int(b[j])+carry
        if tmp==0:carry=0;res[j]='0'
        elif tmp==1:carry=0;res[j]='1'
        elif tmp==2:carry=1;res[j]='0'
        elif tmp==3:carry=1;res[j]='1'
        j -= 1
    if carry==0:
        return ''.join(res[1:])
    else:
        res[j] = '1'
        return ''.join(res)






if __name__ == '__main__':

    # res = addBinary('11','1')
    # print(res)
    stack = [1,2,3]
    stack.pop(2)
    print(stack)