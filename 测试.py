import heapq
def heapq_int():
    heap = []
    #以堆的形式插入堆
    heapq.heappush(heap,10)
    heapq.heappush(heap,1)
    heapq.heappush(heap,10/2)
    [heapq.heappush(heap,i) for i in  range(10)]
    [heapq.heappush(heap,10 - i) for i in  range(10)]
    #最大的10个元素
    # print(heapq.nlargest(10,heap))
    #输出所有元素
    print([heapq.heappop(heap) for i in range(len(heap))])

if __name__ == '__main__':
    heapq_int()