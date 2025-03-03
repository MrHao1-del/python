'''
name='传智播客'
stock_price=19.99
stock_code="003032"
stock_price_daily_growth_factor=1.2
growth_day=7
later_stock_price=stock_price*1.2**7
print(f"公司：{name}，股票代码：{stock_code}。当前股票：{stock_price}","每日增长系数是：%.2f，经过%d天的增长后，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_day,later_stock_price),sep="\n")

user_name=input("请输入用户名：")
user_type=input("请输入用户身份：")
print(f"你好，{user_name},你是尊贵的：{user_type}，欢迎你的光临")

print("欢迎来到游乐场。")
if int(input("请输入你的年龄："))>=12:
    print("享受八折优惠")
elif int(input("请输入你的vip等级:"))>=3:
    print("享受七折优惠")
else:
    print("免费游玩")
print("祝您游玩愉快")

import random as r
answer=r.randint(1, 100)
max_num=100
min_num=1
print("答案在1到100之间")
while True:
 num=int(input("请输入你猜测的数字:"))
 if answer==num:
    print("恭喜你猜对了，游戏结束")
    break
 else:
  if num>answer:
    max_num=num
    print(f"答案在{min_num}到{max_num}之间")
  elif num<answer:
    min_num=num
    print(f"答案在{min_num}到{max_num}之间")

import random as r
answer = r.randint(1, 100)  # 生成整数答案
max_num = 100
min_num = 1
remaining_guesses = 10
success = False  # 是否猜中的标记
while remaining_guesses > 0:
    try:
        num = int(input(f"请输入{min_num}到{max_num}之间的数字（剩余次数：{remaining_guesses}）:"))
        if num < min_num or num > max_num:
            print(f"请输入{min_num}到{max_num}之间的数字！")
            continue  # 不扣除次数
        remaining_guesses -= 1  # 扣除一次机会
        if num == answer:
            print("恭喜你猜对了，游戏结束")
            success = True
            break
        elif num > answer:
            max_num = num
        else:
            min_num = num
        print(f"答案在{min_num}到{max_num}之间")
    except ValueError:
        print("请输入有效的整数！")
if not success:
    print(f"很遗憾，机会用完了。正确答案是{answer}。")

i=1
sum=0
while i<=100:
    sum+=i
    i+=1
print(f"总和为：{sum}")

i=1
while i<=9:
    j=1
    while j<=i:
        print("%d*%d=%d\t"%(i,j,i*j),end='')
        j+=1
    i+=1
    print()

name="dhjlaksufjiosaf,aidhyaofhas"
i=0
for x in name:
  if x=="a":
      i+=1
print(f"一共有{i}个a")

i=0
num=int(input("请输入一个数字："))
for x in range(1,num):
    if x%2==0:
        i+=1
print(f"一共有{i}个偶数")

i=0
for i in range(5):
    print(i)
print(i)

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}",end=" ")
    print()

import random as r
money=10000
for i in range(1,21):
    grade = r.randint(1, 10)
    if money<=0:
        print("工资发完了，下个月领取")
        break
    elif grade<5:
        print(f"员工{i},绩效分{grade}，低于5，，下一位")
        continue
    else:
        money-=1000
        print(f"向员工{i}发放工资1000元，账户余额{money}元")

def healthy_check():
    print("请出示你的健康码")
healthy_check()

def mat(x,y):
    result=x**y
    print(f"结果是{x**y}")
mat(2,3)

a=10
if a>11 or 0:
    print("aaa")
else:
    print("bbb")

money=50000
name=input("请输入你的名字：")
def check_banlance():
    print(f"{name}，你好，你的余额为：{money}")

def deposit():
    global money
    de_money= int(input(f"存款的数额为（单位元）："))
    money+=de_money
    print(f"{name}，你好，你存款{de_money}元成功")
    check_banlance()
def draw_money():
    global money
    while True:
      dr_money = int(input("取款的数额为："))
      if dr_money<=money:
         break
      else:
         print("余额不足，请重新输入")
    money-=dr_money
    print(f"{name}，你好，你取款{dr_money}元成功")
    check_banlance()
def main_menu():
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入你的选择:"))
while True:
    num=main_menu()
    if num==1:
        check_banlance()
        continue
    elif num==2:
        deposit()
        continue
    elif num==3:
        draw_money()
        continue
    else:
        break

my_list=["liudehua","zhangxueyou"]
print(my_list)
#查找某元素在列表中的下标索引
two_list=[[1,2,3],[2,3,4],[3,4,5]]
place=two_list.index([1,2,3])
print(f"{place}")
#修改特定下标索引的值
two_list[0]=[2,3,4]
print(f"{two_list}")
#在指定位置插入新元素
two_list.insert(1,[1,2,3])
print(two_list)
#在列表的尾部追加单个新元素
two_list.append([4,5,6])
print(two_list)
#在列表尾部追加一批元素
three_list=[1,2,3]
two_list.extend(three_list)#extend(其他数据容器)
print(two_list)
#元素的删除
two_list=[[1,2,3],[2,3,4],[3,4,5]]
del two_list[0] #del为关键字
print(two_list)
two_list=[[1,2,3],[2,3,4],[3,4,5]]
new_two_list=two_list.pop(0)
print(new_two_list,two_list,sep="\n")
#删除某元素在列表中的第一个匹配项
two_list=[1,2,3,3]
two_list.remove(3)
print(two_list)
#清空列表
two_list.clear()
print(two_list)
#统计列表某个元素的数量
two_list=[[1,2,3],[2,3,4],[3,4,5]]
a=two_list.count([1,2,3])
print(a)
#统计列表中总共元素的数量
lenth=len(two_list)
print(lenth)

age_list=[21,25,21,23,22,20]
age_list.append(31)
age_list.extend([29,33,30])
age_list.remove(21)
age_list.remove(30)
num=age_list.index(31)
print(age_list,num)

k=0
num2=[]
num3=[]
num1=[1,2,3,4,5,6,7,8,9,10]
for element in num1:
    if element%2==0:
       num2.append(element)
print(f"通过for循环，从列表{num1}中取出偶数，组成的新列表：{num2}")
while k<len(num1):
    if num1[k]%2==0:
        num3.append(num1[k])
    k+=1
print(f"通过while循环，从列表{num1}中取出偶数，组成的新列表：{num3}")

#定义元组
tuple1=(1,"hello",True)
tuple2=()
tuple3=tuple()
print(f"tuple1的类型是{type(tuple1)}")
tuple4=("hello")
print(f"tuple4的类型是{type(tuple4)}")
tuple4=("hello",)#定义的元组只有一个元素时，要在后面加上逗号，否则视为字符串
print(f"tuple4的类型是{type(tuple4)}")
#元组的嵌套
tuple5=((1,2,3),(4,5,6))
#下标索引取出内容
print(tuple5[1][1])

name='周杰伦'
age=11
hobby=["football",'music']
t1=(name,age,hobby)
num=t1.index(age)
name=t1[0]
del hobby[0]
hobby=hobby.append("coding")
print(t1,num)
'''
'''
n="\tdadsn"
num=len(n)
print(num,n[5])
#字符串同元组一样不可修改
'''
'''
#replace方法
str1="itt"
str2=str1.replace("it","i")#replace是产生一个新的字符串
print(str2)
#strip方法
my_str=("  it and hm")
new_my_str=my_str.strip(" ")#不传入参数，默认去除首尾空格
print(new_my_str)
my_str=("12it and hm21")
new_my_str=my_str.strip("12")
print(new_my_str)

str1=("itheima itcast buxuegu")
num=str1.count("it")
print(num)
str2=str1.replace(" ","|")
print(str2)
list3=str2.split("|")
print(list3)

#my_list=[1,2,3,4,5,6]
#my_list=my_list+[6]
#print(my_list)
#my_set={'sd','fw',12}
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)#集合一有而集合二没有的
print(set3)
print(set1)
print(set2)
set1.difference_update(set2)
print(set1)
print(set2)

set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)

my_dict={"周杰伦":91,"林俊杰":92,"胡博文":59}
my_dict1=my_dict.keys()
print(my_dict1,type(my_dict1))
for key in my_dict1:
    print(key)
my_dict["周杰伦"]=33
del my_dict["胡博文"]
print(my_dict)

char={"王力宏":{"部门":'科技部',"工资":3000,"级别":1},
      "周杰伦": {"部门":'市场部',"工资":5000,"级别":2},
      "林俊杰":{"部门":'市场部',"工资":7000,"级别":3},
      "张学友":{"部门":'科技部',"工资":4000,"级别":1},
      "刘德华":{"部门":'市场部',"工资":6000,"级别":2}
      }
for key in char:
    print(key,":",char[key])
    if  (char[key]["级别"])==1:
        char[key]["工资"]+=1000
        char[key]["级别"]+=1
print()
for key in char:
    print(key,":",char[key])
'''
#include<stdio.h>


