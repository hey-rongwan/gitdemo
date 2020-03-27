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

#解密问题
s=input()           #输入一串密文
f={'0001':'A','0010':'B','0011':'C','0000':'D','0100':'E','1111':'F','0101':'G','1001':'H'}  创建编码字典
a=len(s)            #用len函数求出s的长度
c=''                #创建空白字符串c
for i in range(0,a,4):   #以4为步长进行循环
    x=s[i:i+4]       #每一次循环得到一个s中长度为4的密文x
if x not in f:      
        c='Not Found!'  #若x不在f中，输出字符串“Not Found！”结束
        break
    else:               #否则，输出x为键在字典f中对应的值所组成的字符串
        c+=f[x]
print(c)