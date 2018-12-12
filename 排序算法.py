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







































#  它的工作原理是通过构建有序序列，
#       对于未排序数据，在已排序序列中从后向前扫描，
#       找到相应位置并插入。
#       插入排序在实现上，
#       通常采用in-place排序（即只需用到O(1)的额外空间的排序），
#       因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。



#  开始排序， 先从列表中抽取第一个值1，
#            再抽取第二个值2，与值1比较，
#            如果   值2 < 值1 则值2插入到值1的前面(值1=值2，值2=值1)，否则不改变。
#            抽取值3，如果值3 < 值2 则插入到值2的前面（值3=值2，值2=值3），
#            ...
# 
# 左手是空的，牌面朝下放在桌上。           
#     接着，一次从桌上摸起一张牌，并将它插入到左手一把牌中的正确位置上。
#     为了找到这张牌的正确位置，要将它与手中已有的牌从右到左地进行比较。
#     无论什么时候，左手中的牌都是排好序的。 
'''
def insert_sort(lst):
    n=len(lst)
    if n==1: return lst
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]: lst[j],lst[j-1]=lst[j-1],lst[j]
            else:break
    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst
'''

# test = [84, 44, 28, 60, 16, 76, 0, 20, 32, 12, 52, 72, 56, 36, 80, 64, 88, 48, 8, 40, 4, 96, 68, 24, 92]
# print("改变前----->  ",test)
# for i in range(len(test)):
#     tmp = test[i]
#     j = i - 1
#     while j >= 0 and tmp < test[j]:
#         test[j + 1 ] = test[j]
#         j -= 1
#     # test[j+1] = tmp 

# print("改变后----->  ",test)

