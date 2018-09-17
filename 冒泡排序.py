def bubble_sort(li):
    i = len(li)-1
    while i>0:
        j = 0
        while j<i:
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
            j+=1
        i-=1


if __name__ == '__main__':
    li = [1,2,5,4,7,8,10,2,4]
    bubble_sort(li)
    print(li)