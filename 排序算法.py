import random
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

if __name__ == "__main__":
    # MaoPao()
    ChaRu()
