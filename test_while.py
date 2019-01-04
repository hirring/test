"""
while 循环
Python中while语句的一般形式：

while 判断条件：
    语句


同样需要注意冒号和缩进。另外，在Python中没有do..while循环。

以下实例使用了 while 来计算 1 到 100 的总和：
"""
#!/usr/bin/env python3
"""
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))
"""
#执行结果如下：

#1 到 100 之和为: 5050

#无限循环
#我们可以通过设置条件表达式永远不为 false 来实现无限循环，实例如下：

#实例

"""
var = 1
while var == 1 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print ("你输入的数字是: ", num)
 
print ("Good bye!")

#执行以上脚本，输出结果如下：
"""
"""
输入一个数字  :5
你输入的数字是:  5
输入一个数字  :
你可以使用 CTRL+C 来退出当前的无限循环。
无限循环在服务器上客户端的实时请求非常有用。
"""




