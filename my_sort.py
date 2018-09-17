class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False
        m, n = len(matrix), len(matrix[0])
        start, end = 0, m * n - 1
        while start <= end:
            mid = (start + end) // 2
            num = matrix[mid//n][mid%n]
            if num==target:return True
            elif num < target:
                start = mid + 1
            else:
                end = mid - 1



def partition(array, left, right): # 不断地寻找新的pivot
    if left >= right:
        return
    pivot = array[left]
    while left < right:
        while left < right and array[right] > pivot:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= pivot:
            left += 1
        array[right] = array[left]
    array[right] = pivot   # 此时left==right
    return left

def quick_sort(array,l,r):  # 采用栈实现非递归方式，需要使用partition定位
    if l >= r:return
    stack =[]
    stack.append(r)
    stack.append(l)
    while stack:
        i = stack.pop()
        j = stack.pop()
        if i<j:
            k = partition(array,i,j)
            if k<j:
                stack.append(j)
                stack.append(k+1)
            if i<k:
                stack.append(k-1)
                stack.append(i)



if __name__ == '__main__':
    # sol = Solution()
    m = [2,3,4,1,80,9,5]

    quick_sort(m,0,6)
    print(m)