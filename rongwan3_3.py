#解决新北京地铁问题
#创建：荣婉
#日期：2018.4.11
n1,n2,n3=map(int,input().split())    #用split函数单行输入三个分离整数
a1=0                          #用a1、a2、a3分别表示第1、2、3天的乘车总价
a2=0
a3=0
for i in range(1,n1+1):        #输入n1行数据，每行输入第一天单次乘车价格
    i1=int(input())
    a1=a1+i1               #将每一次的乘车价格加到a1，得到第一天的乘车总价
for i in range(1,n2+1):
    j1=int(input())
    a2=a2+j1
for i in range(1,n3+1):
    k1=int(input())
    a3=a3+k1