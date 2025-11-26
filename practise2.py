list1 = [0,1,2,3,4,5,6,7,8,9,10]
list2 = ['a','b','c','d','e']

print("原始列表list1:", list1)
print("list1[2:4]:", list1[2:4])          #從索引2開始到索引4結束，但不包含索引4
print("list1[:3]:", list1[:3])            #從索引0開始到索引3結束，但不包含索引3
print("list1[2:]:", list1[2:])            #從索引2開始到列表結束
print("list1[:-2]:", list1[:-2])          #從索引0開始到倒數第2個元素結束，但不包含倒數第2個元素
print("list1[-3:]:", list1[-3:])          #從倒數第3個元素開始到列表結束
print("list1[:],:", list1[:])             #從索引0開始到列表結束
print("list1[::2]:", list1[::2])          #從索引0開始到列表結束，步長為2

print("list1[max] :",max(list1))               #列表中的最大值
print("list1[min] :",min(list1))               #列表中的最小值
print("list1[len]:",len(list1))              #列表的長度
print("list1[sum] :",sum(list1))               #列表中所有元素的和
