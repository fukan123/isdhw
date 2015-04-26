
from math import ceil
x=int(input("输入要查找的数字："))
low=0
arry=[1,2,3,4,5,6,7,8,9,10]
high=len(arry)-1
i=0
while(low<high):
    i=i+1
    mid=(low+high)/2
    mid= int(ceil(mid))
    print('查找次数。',i)
    print('the mid is',mid)
    print('the mid value is',arry[mid])
    if x==arry[mid]:
        print('值已经查找到：',arry[mid])
        break
    elif x>arry[mid]:
        low=mid
    else:
        high=mid
if low>=high:
    print('failure')


