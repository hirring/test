"""
age = int(input("犬の年齢を入力してください"))
print("")
if age < 0:
    print("Are you kindding me?")
elif age == 1:
    print("人間の14歳に相当する")
elif age == 2:
    print("人間の22歳に相当する")
elif age > 2:
    human = 22 + (age -2)*5
    print("人間に相当する年齢は",human)

input("enterキーを押すと戻る")
"""



"""
以下为if中常用的操作运算符:

操作符	描述
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较对象是否相等
!=	不等于
"""
"""
# 程序演示了 == 操作符
# 使用数字
print(5 == 6)
# 使用变量
x = 5
y = 8
print(x == y)

"""
"""
以上实例输出结果：

False
False
"""

# 该实例演示了数字猜谜游戏
"""
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))
 
    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")
"""

#执行以上脚本，实例输出结果如下：
"""
$ python3 high_low.py 
数字猜谜游戏!
请输入你猜的数字：1
猜的数字小了...
请输入你猜的数字：9
猜的数字大了...
请输入你猜的数字：7
恭喜，你猜对了！
"""

"""
if 嵌套
在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。

if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
"""

#if else 嵌套实例
# !/usr/bin/python3

"""
num=int(input("输入一个数字："))
if num%2==0:
    if num%3==0:
        print ("你输入的数字可以整除 2 和 3")
    else:
        print ("你输入的数字可以整除 2，但不能整除 3")
else:
    if num%3==0:
        print ("你输入的数字可以整除 3，但不能整除 2")
    else:
        print  ("你输入的数字不能整除 2 和 3")

"""

account = 'abc'
password = '123456'
#constant 常量,python中的常量不是真正意义的常量，区分大小写。
#module 模块（一个文件）一个Python项目是由多个模块形成，每个模块可以加上文字说明
#

print("plesse input account")
user_account = input()

print("password")
user_password = input()
 
if account == user_account and password == user_password :#比较运算符前后空格
    print("success")
else :
    print("fail")
#######################################
#snippet 片段
#
"""
if condition:
    pass # pass 表示 空语句 或者 占位语句，若没有会报错
else:
    pass

###########################
a = True

if a :
    print('')
else :      
    print('')

from django.utils.translation import ugettext_lazy as _
for target_list in expression_list:
    pass
else:
    pass
"""

if True: 
    pass
if condition:
    code1 
        code11
        code22
    code2
    code3 ##代码块，伪代码，表示一种思路
else:
    code1
    code2
    code3
## 同级别的代码块是全部会被执行，python中没有goto（改变代码执行顺讯）
## 最好不要嵌套太多，推荐将子代码提取成函数

##########################################
