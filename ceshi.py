#解决缩写问题
#创建者：荣婉
#创建时间：2018年4月11日
a=input().upper()      #输入一段英文全称并用upper函数将其全部转化为大写，组成列表a
b=[]                #创建空白列表b
for i in range(len(a)):   #遍历a列表中元素，
    if a[i] not in b:    #并将a列表中不同的元素复制到b列表中
        b.append(a[i])
print(len(b)-1)      #用len函数求列表b的长度，由于从0算起，减1得a中用到的字母种类数
c=a.split()         #用split函数将a中的元素分块并组成列表c
d=[]              #创建空列表d
for j in range(len(c)):                      #遍历c中元素
if c[j] not in ['AND','THE','FOR','OF']:    #将c中非“AND”,“THE”，“FOR”,“OF”的词块的首个字母添加进d中
        d.append(c[j][0])
for k in range(len(d)):                     #遍历并返回d中每一个元素
    print(d[k],end='')