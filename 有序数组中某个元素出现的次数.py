
#  先求出该值在列表中首次和最后一次出现的index，然后相减即可

def get_index(li,val,isLeft=True):
    left = 0
    right = len(li)-1
    last = 0
    while left<=right:
        mid = (left+right)//2
        if li[mid]<val:
            left = mid+1
        elif li[mid]>val:
            right = mid-1
        else:
            last = mid
            if isLeft:
                right = mid - 1
            else:
                left = mid + 1
    return last if last>0 else -1



if __name__ == '__main__':
    # l = [1,2,3,3,4,5,6]
    # print(count(l,3))
    l = [1,2,3,4,5,5,5,6,6,7]
    val = 6
    left_index = get_index(l,val,True)
    right_index = get_index(l,val,False)
    print(right_index-left_index+1)