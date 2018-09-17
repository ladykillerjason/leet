def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if not nums:return False
    dic = {}
    for i,v in enumerate(nums):
        if v in dic.keys() and i-dic[v]<=k:return True
        dic[v]=i
    return False



if __name__ == '__main__':

    nums =[5,6,3,2,7,4,8,2]
    k = 3
    res = containsNearbyDuplicate(nums,k)
    print(res)