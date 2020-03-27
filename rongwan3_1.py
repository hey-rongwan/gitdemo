#加密问题
#创建者：荣婉
#日期：2018.4.11
a=list(input().split())        #输入原字符并返回为列表s
b=list(input().split())        #输入原字符对应的密文并返回为列表b
c={}                     #创建空白列表c
for i in range(len(a)):        #用len函数计算并返回列表a的长度，遍历a中字符，
    c[a[i]]=b[i]            #将a中i位置字符与b中i位置字符对应起来并储存在c   
d=input()                 #输入要加密的字符并返回为列表d
f=''                      #创建空字符串f
for i in range(len(d)):        #遍历d中字符并将d中i位置字符赋值为a中相同字符所
    f+='{}'.format(c[d[i]])   #相同字符所对应的b中字符，添加进f中
print(f)                   #输出f，即得加密后字符串