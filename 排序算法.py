import random
import time
def ChaRu():
    list1 = [x for x in range(0,100,4)]
    random.shuffle(list1)
    print("排序前的 list：",list1)

    # 冒泡排序
    for j in range(len(list1)-1,0,-1):
        for i in range(j):
            if list1[i] > list1[i+1]:
                list1[i+1],list1[i]  = list1[i],list1[i+1]

    # 插入排序
    for i in range(len(list1)):
        tmp = list1[i]     
        j = i - 1    
        while j >= 0 and tmp < list1[j]:  # list[j] 是左边的值，tmp是右边的值，  tmp 小于 list[j]
            list1[j+1] = list1[j]         # list1[j+1] 是右边的值，等于左边的值
            j -= 1                        # 只一次左移只能把当前元素移一个位置 ,继续左移直到此元素放到排序好的列表的适当位置为止
        list1[j+1] = tmp

    print("排序后的 list：",list1)

def selection_sort(arr):
    for i in range(len(arr) - 1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i + 1, len(arr)):
            m = time.strptime(list(arr[j].values())[0], "%Y-%m-%dT%H:%M:%S.000Z")
            a = int(time.mktime(m))
            n = time.strptime(list(arr[minIndex].values())[0], "%Y-%m-%dT%H:%M:%S.000Z")
            n = int(time.mktime(n))
            if a < n:
                minIndex = j
        # i 不是最小数时，将 i 和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

if __name__ == '__main__':
    lists = [
        {'小王': '2020-06-29T04:24:16.000Z'},
        {'小二': '2020-01-21T09:36:47.000Z'}, 
        {'小张': '2020-06-23T08:09:11.000Z'},
        {'小宝': '2020-04-27T09:36:47.000Z'}, 
        {'小亖': '2020-05-27T09:36:47.000Z'}, 
        {'小刚': '2020-05-17T09:36:47.000Z'},
    ]
    result = selectionSort(lists)
    print(result)
    ChaRu()
